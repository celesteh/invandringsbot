# invandringsbot
When people post ignorant tweets about immigration, this bot replies with a rant about the moral responsibility we all have to welcome refugees. This fork has been translated into American English.

# Social Requirements

Please note that in order for this to be effective, the bot account
should have a white person as a user icon and a name that sounds
white or pro-Trump. An icon of Trump holding the bible is included.

The bot MUST also have a few hundred followers or it may be counter-productive. To get followers, you may either purchase them or grow your follower account more organically, by posting a few tweets with the #MAGA hashtag and following others who use it. Many users of this hashtag are also bots and will automatically follow you back. Also try #TrumpTrain and especially #VoteTrump. Any account still posting about the need to vote is almost certainly a bot. Click on the 'Who to follow' recommendations, as well.

Ensure that your bot has at least a small handful of tweets before you begin. These should either be innocuous or demonstrating membership of the pro-Trump or evangelical milieu.

# How it works

Whenever anyone tweets a tweet containing a certain trigger word or phrase, invandringsbot will reply with a admonishment.

In this specific, forked implementation of invandringsbot, the trigger word is "rapefugee" and the rant is about the moral responsibility we have to welcome refugees. However, the trigger word can be anything, as can the admonishment be.

# Translate into your language/ take on another issue!

It's not only Swedes and xenophobes who are in need of a admonishment about our moral responsibilities. Make the world a better place by translating invandringsbot!

# Getting started:

You will need python and [Twython](https://github.com/ryanmcgrath/twython). Click for details on how to install.

1. Create (or repurpose) a twitter account. (See social requirements above).
2. Fork this repository.
3. Rename the `apikeys_template.py` file to `apikeys.py`, and add your Twitter API keys as obtained from apps.twitter.com.
4. Open the `setup.py` file. Fill in your trigger word, rant, and the Twitter handle of the bot.
5. To start following some accounts, open your terminal application, switch to the directory (folder) of the project and type 'python3 auto_follow.py' . This will take HOURS to run.
6. Using the web or other interface, log into the account and make some tweets about the weather, the season, the wonderfulness of the pledge of allegiance, or any topic that is either apolitical or right wing (but victimless)
7. Set up a cron job to run 'python3 once_daily.py' once a day or once every few days (or do this by hand)
8. Follow a lot of #TrumpTrain accounts and companies who may follow back. Retweet people in the Trump milieu making harmless tweets.
9. Wait until you have followers before you go on! You do not want to look like an egg account.

# After you have followers

Now, start invandringsbot by calling `python3 mainbot.py`, when in the correct directory in your terminal.

# Dependencies

Using python 3. Has not been tested on python 2, but should work with minor optimizations.

- [Twython](https://github.com/ryanmcgrath/twython). Used for all contact with the Twitter API.
