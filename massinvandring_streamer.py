# the MassinvandringStreamer is a subclass of TwythonStreamer
from twython import TwythonStreamer
# import twythonaccess, to be able to send tweets
import twythonaccess
# import the setup file with the trigger word and rant
import setup
# import regex, to be able to filter out sarcastic tweets
import re
import glob
import random
import time
import apikeys

# the MassinvandringStreamer class will use the streaming api to find tweets containing the word 'massinvandring'
# This class could technically be used to reply to all kinds of tweets.
class MassinvandringStreamer(TwythonStreamer):

    # only reply to one user once
    replied_to_users = []

    # users from previous returns
    files = glob.glob("data/*.csv")

    awake = 0
    last_act = 0


    def check_duplicate (self, id_str ):

        duplicate = False

        if id_str in self.replied_to_users:
            duplicate = True

        if not duplicate:
            for csv_file in self.files:
                with open(csv_file, 'r') as losers:
                    for twerp in losers:
                        twerp = twerp.rstrip()
                        #print twerp + ' ' + id_str

                        if twerp == id_str:
                            duplicate = True
                            break
                if duplicate:
                    break
        return duplicate



    def dump_blocks (self):
        #global blocked
        if len(self.replied_to_users) > 0:
            #try:
                f = file('data/block_list'+ str(time.time())+'.csv', 'w')
                for item in self.replied_to_users:
                    f.write(str(item)+'\n')
                f.close()
                self.replied_to_users = []
                self.files = glob.glob("data/block_list*.csv")
            #except Exception, e:
                #do_exception('file writing')


    # this function will be called when a tweet is received
    def on_success(self, tweet):
        # generate a reply

        #print tweet['text']

        # first check so trigger words aren't in quotes
        # or in quoted tweets
        # this is to remove tweets that aren't genuinely xenophobic
        # it can be in a quoted phrase
        found = False
        for trigger_word in setup.trigger_words.split(","):
            if trigger_word in tweet["text"]:
                found = True

            if re.search(r'["\'].*' + trigger_word + r'.*["\']', tweet["text"]):
                return

        if not found:
            # must have been in a quoted tweet
            return

        # if tweet is from self, return here
        if tweet["user"]["screen_name"] == apikeys.screen_name:
            return
        # tweet mentions me
        if (apikeys.screen_name in tweet['text']):
            return
        #tweet is in reply to me
        if tweet['in_reply_to_screen_name'] == apikeys.screen_name:
            return

        #if tweet["user"]["id"] in self.replied_to_users:
        if self.check_duplicate(tweet["user"]["id"]):
            return


        #exclude retweets
        if "retweeted_status" in tweet: #tweet["retweeted_status"]:
            #print "retweet"
            #print tweet["id"]
            #print tweet["user"]["screen_name"]
            return
        # user isn't being obviously ironic or critical

        if time.time() < self.awake:
            if (time.time() - self.last_act) > (110 * 60):
                twythonaccess.set_sleep(False)
                twythonaccess.seem_normal()
                twythonaccess.set_sleep(True)
                self.last_act = time.time()
            return

        twythonaccess.set_sleep(False)
        print str(tweet["user"]["screen_name"]) + ' ' + tweet["text"]

        #reply = content.construct_tweet(setup.callouts)
        #for index, reply in enumerate(replies):
        #    replies[index] = "@" + tweet["user"]["screen_name"] + " " + reply


        # try to send the reply (not guaranteed)
        #if twythonaccess.send_rant(tweets = replies, in_reply_to_status_id = tweet["id"]):
        #reply = "@" + tweet["user"]["screen_name"] + " " + content.construct_tweet(setup.callouts)

        #print tweet["id"]
        #print reply

        #next 3 lines commented for testing
        #twythonaccess.send_tweet(tweet=reply,  in_reply_to_status_id=tweet["id"])
        try:
            #if twythonaccess.send_rant(tweets = [reply], in_reply_to_status_id = tweet["id"]):
            if twythonaccess.do_reply(tweet):
                self.replied_to_users.append(tweet["user"]["id"])
                self.replied_to_users.sort()
                twythonaccess.set_sleep(True)
                self.last_act = time.time()
                self.awake = self.last_act + (4 * 60 * 60) + (60 * 60 * random.random())


                time.sleep((3*60) + (120 * random.random()))
                twythonaccess.set_sleep(False)
                twythonaccess.seem_normal()
                twythonaccess.set_sleep(True)
                #i=0
                #while (i < 2):
                #    time.sleep((110* 60) + (600*random.random()))
                #    twythonaccess.set_sleep(False)
                #    twythonaccess.seem_normal()
                #    twythonaccess.set_sleep(True)
                #    i = i + 1
                #twythonaccess.set_sleep(False)
        except Exception, e:
            self.dump_blocks()
            self.on_error(str(0), str(e))


    # when an error is caught
    def on_error(self, status_code, data):
        print("STREAMING API ERROR!")
        print("Status code:")
        print(status_code)
        print("Other data:")
        print(data)
        print("END OF ERROR MESSAGE")
        self.dump_blocks()
