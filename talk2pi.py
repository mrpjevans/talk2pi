import snowboydecoder
import sys
import signal
import re
import ResumableMicrophoneStream
from google.cloud import speech

# Google audio recording parameters and config
SAMPLE_RATE = 16000
CHUNK_SIZE = int(SAMPLE_RATE / 10)  # 100ms
STREAMING_LIMIT = 240000  # 4 minutes

client = speech.SpeechClient()
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=SAMPLE_RATE,
    language_code="en-US",
    max_alternatives=1,
)
streaming_config = speech.StreamingRecognitionConfig(
    config=config, interim_results=True
)

# Snowboy object placeholder
snowboy = None

# Basic commandline checking
if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python talk2pi.py your.model")
    sys.exit(-1)

# Path to the hotword model file
model = sys.argv[1]


def start_snowboy():
    global snowboy
    snowboy = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Listening for hotword')
    snowboy.start(detected_callback=start_google_capture)


def listen_print_loop(responses, stream):

    for response in responses:

        if ResumableMicrophoneStream.get_current_time() - stream.start_time > STREAMING_LIMIT:
            break

        if not response.results:
            continue

        result = response.results[0]

        if not result.alternatives:
            continue

        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        if result.is_final:
            sys.stdout.write(transcript + "\n")
            return transcript

        else:
            sys.stdout.write(transcript + "\r")


def start_google_capture():
    global snowboy

    # Stop Snowboy to free up the audio device
    snowboy.terminate()

    # Start streaming to Google
    mic_manager = ResumableMicrophoneStream.ResumableMicrophoneStream(
        SAMPLE_RATE, CHUNK_SIZE)

    print('Listening to command...')

    with mic_manager as stream:

        sys.stdout.write(
            "\n" + str(STREAMING_LIMIT *
                       stream.restart_counter) + ": NEW REQUEST\n"
        )

        stream.audio_input = []
        audio_generator = stream.generator()

        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(
            requests=requests, config=streaming_config
        )

        # Listen and transcribe
        transcript = listen_print_loop(responses, stream)

        print("Processing: " + transcript)

        # Close down and resume listening for hotword
        stream._audio_stream.stop_stream()
        stream._audio_stream.close()
        start_snowboy()


start_snowboy()
