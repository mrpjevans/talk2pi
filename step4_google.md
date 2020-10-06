## Setting up Google Speech-To-Text API

You will need a Google account and you will have to provide billing information
(although the chances of you ever being charged are pretty slim!)

- Go to <https://console.developers.google.com/>

- If not prompted automatically, click on the dropdown next to 'Google APIs' and
  select select 'New Project' in the resulting modal window

- Give your project a name

- Leave location as default

- Click 'Create'

- It'll take a few seconds to create the project. When the notification appears click 'Select Project'
  or choose it from the dropdown list.

- Click 'Enable APIs and Services'

- In the search box enter 'speech'

- Choose 'Cloud Speech-To-Text API'

- Click 'Enable'

- If you do not have a billing account you will now be asked to create one. This is because
  there are charges for any usage over one hour of transcription per month.

- When you get to the API's page you wil be prompted to create credentials. Click the button.

- Select the 'Cloud Speech-To-Text API' in the first dropdown box

- In the second block of text, choose 'No, I'm not using them'

- Click 'What credentials do I need?'

- You will now create a 'service account'

- Give it a name (same as the project is fine)

- Choose a role of 'Project > Owner'

- Leave the key type as JSON

- Click 'Continue'

- A file ending `.json` will be downloaded to your local computer

- If you are not on the Raspberry Pi, transfer the file over now

## Installing

To install the Speech-To-Text SDK:

```bash
pip3 install google-cloud-speech
```

## Testing

To test your access to the Google API, you can download their test applications:

```bash
cd
git clone https://github.com/googleapis/python-speech.git
cd python-speech/samples/microphone
```

- You now need to set the environment variable for your Google credentials file:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/[YOUR FILE].json"
```

- Change [YOUR FILE] to the filename of the credentials file

Now you can run a transcribing demonstration:

```bash
python3 transcribe_streaming_infinite.py
```

Let it start up (you can ignore the many errors, it's just trying to find a micrphone it can use), and try speaking. You should get
a transcription on-screen of everything you've said!
