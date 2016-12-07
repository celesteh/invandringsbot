# Import the twythonaccess
import twythonaccess
from twython import Twython
# import the setup file
import setup
# import the streamer
# import the apikeys to be able to authenticate
import apikeys


# the main function will be called when this script is called in terminal
# the bash command "python3 once_daily.py" will call this function
def main():
    twitter = Twython(apikeys.CONSUMER_KEY, apikeys.CONSUMER_SECRET, apikeys.ACCESS_TOKEN, apikeys.ACCESS_TOKEN_SECRET)

    twitter.update_status(status=setup.non_reply)


# if called directly (as in "python3 mainbot.py"), then call main() function
if __name__ == "__main__":
    main()
