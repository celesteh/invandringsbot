#!/usr/bin/python

# Import the twythonaccess
import twythonaccess
from twython import Twython
# import the setup file
import setup
# import the streamer
from massinvandring_streamer import MassinvandringStreamer
# import the apikeys to be able to authenticate
import apikeys
import time
import random
import content
import setup
import setproctitle


# the main function will be called when this script is called in terminal
# the bash command "python3 mainbot.py" will call this function
def main():

    setproctitle.setproctitle('invandringsbot')


    # check if bot has enough followers_count

    while True:
        try:

            while (twythonaccess.get_followers_count() < 501) or setup.on_probation:
                twythonaccess.post_content()
                twythonaccess.follow_a_user()
                time.sleep(60 + (300* random.random()))
                twythonaccess.follow_a_user()
                time.sleep((30*60) + (30 * 60 * random.random()))


            # start the streamer, and detect for instances of massinvandring in all Swedish tweets
            streamer = MassinvandringStreamer(apikeys.CONSUMER_KEY, apikeys.CONSUMER_SECRET, apikeys.ACCESS_TOKEN, apikeys.ACCESS_TOKEN_SECRET)
            streamer.statuses.filter(track = setup.trigger_words, language = "en")

        except Exception, e:
            print "Exception in main()"
            print e
            try:
                if streamer is not None:
                    streamer.dump_blocks()
            except Exception, e:
                pass
            print "sleeping"
            time.sleep(60*16 + (60 * random.random()))
            print "continuing..."


# if called directly (as in "python3 mainbot.py"), then call main() function
if __name__ == "__main__":
    main()
