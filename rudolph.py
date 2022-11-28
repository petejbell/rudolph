import secrets
import terms
import time
from gpiozero import LED
from twython import TwythonStreamer

# Search terms
TERMS = '#Christmas'

# GPIO pin number of LED
red = LED(16)

# Twitter application authentication
APP_KEY = secrets.APP_KEY
APP_SECRET = secrets.APP_SECRET
OAUTH_TOKEN = secrets.OAUTH_TOKEN
OAUTH_TOKEN_SECRET = secrets.OAUTH_TOKEN_SECRET

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            # print (data['text'].encode('utf-8'))
            # print ()
            red.on()
            time.sleep(0.5)
            red.off()
# Create streamer
try:
    stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
    pass
