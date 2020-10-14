from datetime import datetime

phrases = ['what time is it']


def trigger(transcript):
    today = datetime.now()
    print("Today's date:", today)
