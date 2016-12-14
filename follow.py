from twython import Twython
import apikeys
import time
import random
import setup

#twitter = Twython(apikeys.CONSUMER_KEY, apikeys.CONSUMER_SECRET, apikeys.ACCESS_TOKEN, apikeys.ACCESS_TOKEN_SECRET)
user_list = None



def get_users(twitter):

    users = ['amrightnow', 'USFreedomArmy' ,'GrateAmerica', apikeys.screen_name,'investisock', 'intellwatch']
    while True:
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
                #time.sleep(300 * random.random())


def do_follow(twitter, user, ifLikely=True):
    #time.sleep(15 + (30* random.random()))
    flag = False

    if user.lower() == apikeys.screen_name.lower():
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
        #print relationship
        #print relationship[0]['connections']
        if "following" not in relationship[0]['connections']:
            print "not following"
            time.sleep(2 + (3 * random.random()))
            twitter.get_user_timeline(screen_name=user, count=5) #Look more human
            time.sleep(10 + (30 * random.random()))
            twitter.create_friendship(screen_name=user)
            flag = True
    except Exception, e:
        print "Exception in follow.do_follow()"
        #print e
        #protected acounts cause exceptions, so do a short sleep
        time.sleep(60+ (60 * random.random()))
        print "continuing..."
    return flag


def follow_a_user(twitter, limit=3):
    global user_list

    #print "user_list " + str(user_list)
    try:
        if user_list is None:
            user_list = get_users(twitter)
            print "got user list"

        flag = False
        tries = 0
        while (not flag) and (tries < limit):
            time.sleep(28 + (6* random.random()))
            next_user = user_list.next()
            print "going to follow " + next_user
            flag = do_follow(twitter, next_user)
            tries = tries + 1

    except Exception, e:
        print "Exception!"
        print e
        time.sleep(30)


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
