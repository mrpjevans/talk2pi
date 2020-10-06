# talk2pi

Talk to your Raspberry PI with ReSpeaker, Snowboy and Google Speech APIs

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

(Confession: These are the insructions but I'm yet to make them work!)

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

Full instructions here: <step2_snowboy.md>

## Set up your Google service

Google's APIs provide near real-time text recognition.

Full instructions here: <step4_google.md>

## Set up talk2pi

TBA
