# Installing and configuring Snowboy

So we are not streming audio to Google 24/7, Snowboy provides offline speech
recognition for trigger words (aka 'hotwords').

<https://snowboy.kitt.ai/>

## Make a model

You need to create a 'model', a digital descrtiption of you saying your trigger word, before
installing Snowboy. This can be done online in a matter of minutes.

- Go to <https://snowboy.kitt.ai/> and Log In (and register if needed)

- Click 'Create Hotword'

- Enter the name of the hotword (it can be anything but choose wisely!), the language
  and add any comments you would like.

- Click 'Record my voice'

- Follow the instructions and make three recordings of you speaking you hotword.

- Once completed, click 'Test the voice'

- You can now check the hotword is being recognised

- When happy, click 'Save and Download'

- A `pdml` (Personal Model) file will be downloaded to you local machine

- If that machine is not your target Raspberry Pi, transfer the file to your
  home directory

## Installation

On the Raspberry Pi, run the following commands (version correct at time of writing):

```bash
cd
wget https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/rpi-arm-raspbian-8.0-1.1.1.tar.bz2
tar xvf rpi-arm-raspbian-8.0-1.1.1.tar.bz2
mv rpi-arm-raspbian-8.0-1.1.1 snowboy
sudo apt install python-pyaudio python3-pyaudio sox libpython2.7 libatlas-base-dev
```

You can now test your model (change the filename to match yours!):

```bash
cd ~/snowboy
python demo.py ~/computer.pmdl
```

_Yes, that right, the demo.py doesn't work in Python 3 right now_

When you say the hotword (and ideally nothing else), the console should respond with `Keyword detected`.

## Create Python3 Version

For full transcription we'll need a Python 3 version. One is included with this repo. To create your
own...

```bash
sudo apt install swig
git clone https://github.com/Kitt-AI/snowboy.git
cd snowboy/swig/Python3
make
```

The required files of `snowboydetect.py` and `_snowboydetect.so` can now be found in this directory.
Replace the existing one and the demo will work with Python 3.
