#
# This is an example 'skill'. Copy it and rename it to make your own.
#

from datetime import datetime

# These are the phrases that will 'trigger' the response
# Make sure they're lower case and add as many as you wish
# Choose wisely
phrases = ['what time is it', 'what\'s the time']

# Always have a trigger function like this
# If you return a text string it will be spoken


def trigger(transcript):
    now = datetime.now()
    timestr = now.strftime('%H %M')
    return 'the time is ' + timestr
