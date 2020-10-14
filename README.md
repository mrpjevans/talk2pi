# talk2pi

Talk to your Raspberry PI with ReSpeaker, Snowboy and Google Speech APIs

## Notice

Some files in this repository have been sourced from others to provide a central place
for every required for this project. Please see individual scripts for copyright information.

## Requirements

- Raspberry Pi 4 (Recommended, but a 3 will be fine)
- ReSpeaker 4-Mic Array by Seeed
- Google account

## Set up OS and ReSpeaker

Start with Raspberry Pi OS Buster Lite <https://raspberrypi.org/downloads> installed

### First Positions

Make sure your on the network and have updated to the latest versions of everything with:

```bash
sudo apt -y update && sudo apt -y full-upgrade
```

### Pre-requisties

Install dependancies:

```bash
sudo apt install git python3-pip
pip3 install spidev
```

### Install Seeed drivers for ReSpeaker

See <https://github.com/respeaker/seeed-voicecard>

```bash
cd
git clone https://github.com/respeaker/seeed-voicecard
cd seeed-voicecard
sudo ./install.sh
sudo reboot
```

### Enable LEDs

Enabled SPI interface:

```bash
sudo raspi-config
```

Go to Interfacing Options > SPI and enable

Install the sample code and test pixels:

```
cd
git clone https://github.com/respeaker/mic_hat.git
cd mic_hat
python3 pixels.py
```

(Confession: These are the instructions but I'm yet to make them work!)

### Test Audio

Check the ReSpeaker has been 'seen' by the OS:

```bash
arecord -l
```

You should see something like:

```
**** List of CAPTURE Hardware Devices ****
card 1: seeed4micvoicec [seeed-4mic-voicecard], device 0: bcm2835-i2s-ac10x-codec0 ac10x-codec.1-003b-0 [bcm2835-i2s-ac10x-codec0 ac10x-codec.1-003b-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

You can try a test recording:

```
arecord -D plughw:CARD=seeed4micvoicec,DEV=0 test.wav
```

Say a few words, then use `Ctrl+C` to stop

Play it back (assuming you're using the Pi's audio jack):

```
aplay -D sysdefault:CARD=Headphones test.wav
```

Please note if you have other devices connected, you may have different identifiers. Use `arecord -L` and `aplay -L` to get the possible values for the `-D` (device) switch.

## Install and configure Snowboy

Snowboy provides the 'hotword' support for triggering 'full' recognition.

Full instructions here: <https://github.com/mrpjevans/talk2pi/blob/main/step2_snowboy.md>

## Set up your Google service

Google's APIs provide near real-time text recognition.

Full instructions here: <https://github.com/mrpjevans/talk2pi/blob/main/step4_google.md>

## Set up talk2pi

talk2pi.py is a starting point for building your own voice-controlled home assistant. It's basically a mash-up
of the Snowboy code and the Google streaming code. With it you can add hooks to run your own code when
certain commands are received.

Start by installing these dependancies (one time):

```bash
pip3 install gTTS pygame
sudo apt install libsox-fmt-mp3 libsdl-1.2 libsdl-mixer1.2
```

To try it out:

```bash
export AUDIODEV=hw:0,0
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/[your file]/json"
python3 talk2pi.py /path/to/hotword-model-file.pmdl
```

You should now be able to say your hotword and the code then 'flips' into Google mode. After
a spoken statement it will go back into hotword mode again.

Try saying "what time is it". If you've got something hooked up to the audio jack, you'll
get a spoken response (using Google's tex-to-speech engine)

Have a look at `skills/tell_time.py` for how to build you own skills.