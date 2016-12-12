from twython import Twython
import apikeys
import time
import random
import setup
import follow

def construct_tweet(template):
    tweet = ""

    for item in template:
        #print tweet
        #print str(item)
        if isinstance(item, list):
            tweet = tweet + str(random.choice(item))
        else:
            tweet = tweet + str(item)

    return tweet



def do_rt(twitter, user):

    done = False

    #twitter = twythonaccess.authorize()
    try:
        if follow.do_follow(twitter, user, False):
            time.sleep(30 + (5 * random.random()))

        timeline = twitter.get_user_timeline(screen_name=user, exclude_replies=True, count=5)

        if len(timeline) > 0:
            tweet = timeline[0]
            #print tweet
            if tweet['retweeted'] is False:

                twitter.retweet(id=tweet['id'])
                print "retweeted"
                return True
    except Exception, e:
        print "Exception in content.do_rt()"
        #print e
        time.sleep(60*16)
        print "continuing..."
    return False

def try_rt(twitter):

    accounts = list(setup.accounts_to_rt)
    random.shuffle(accounts)
    flag = True;

    while flag and (len(accounts) > 0):
        user = accounts.pop()
        print user
        flag = do_rt(twitter, user)
        flag = not flag

    return not flag

def timeline_content(twitter):

    coin = random.random()
    print "coin is " + str(coin)
    result = (coin <= setup.percent_rt) #75% chance true
    if result:
        result = try_rt(twitter)

    if not result:
        return (construct_tweet(random.choice(setup.templates)))

    return None



#def main():
    #do_follow('101FearlessLife', True)
    # follow NFL PJNET_Team
# to rt: AllGreatAgain CuteEmergency AChristLife EmrgencyKittens Vol_Football Titans okcthunder UpTheThunder
    #iterator = follow.get_users(twitter)
    #print iterator.next()
    #print iterator.next()
    #print iterator.next()
    #follow.do_follow(twitter, iterator.next())
    #time.sleep(30)
    #follow.do_follow(twitter, iterator.next())
    #do_rt('Titans')
    #print str(construct_tweet(random.choice(setup.templates)))
    #print random.shuffle(setup.accounts_to_rt)
    #try_rt()
    #timeline_content()
    #print setup.accounts_to_rt


#if __name__ == "__main__":
    #main()
