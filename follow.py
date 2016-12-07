from twython import Twython
import apikeys
import time
import random
import setup

#twitter = Twython(apikeys.CONSUMER_KEY, apikeys.CONSUMER_SECRET, apikeys.ACCESS_TOKEN, apikeys.ACCESS_TOKEN_SECRET)

def get_users(twitter):

    users = ['amrightnow', 'USFreedomArmy' ,'GrateAmerica', setup.screen_name,'investisock' ]
    random.shuffle(users)
    for user in users:
        yield user
        next_cursor = -1

        while(next_cursor):

            search = twitter.get_followers_list(screen_name=user,count=200,cursor=next_cursor)

            for result in search['users']:
                yield result['screen_name']

            next_cursor = search["next_cursor"]

            print "time to sleep"
            time.sleep((60 * 15) + (300 * random.random()))

def do_follow(twitter, user, ifLikely=True):
    #time.sleep(15 + (30* random.random()))
    flag = False

    if user.lower() == setup.screen_name.lower():
        #can't follow yourself
        return False

    try:
        if ifLikely:
            profile = twitter.show_user(screen_name=user)
            #print profile
            if (int(profile['followers_count']) > int((profile['friends_count'])*5)) and int(profile['followers_count']) > 900:
                print "not likely"
                return flag
            time.sleep(2 + (3 * random.random()))
        # check if friendship exists
        relationship = twitter.lookup_friendships(screen_name=user)
        print relationship
        print relationship[0]['connections']
        if "following" not in relationship[0]['connections']:
            print "not following"
            time.sleep(2 + (3 * random.random()))
            twitter.get_user_timeline(screen_name=user, count=5) #Look more human
            time.sleep(10 + (30 * random.random()))
            twitter.create_friendship(screen_name=user)
            flag = True
    except Exception, e:
        print e
        time.sleep(60*16)

    return flag


#def main():
    #do_follow('101FearlessLife', True)
    # follow NFL PJNET_Team
# to rt: AllGreatAgain CuteEmergency AChristLife EmrgencyKittens Vol_Football Titans okcthunder UpTheThunder
#    iterator = get_users()
#    print iterator.next()
#    print iterator.next()
#    print iterator.next()


#if __name__ == "__main__":
#    main()
