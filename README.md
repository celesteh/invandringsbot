# invandringsbot
When people post ignorant tweets about immigration, this bot replies with a rant about the moral responsibility we all have to welcome refugees. This fork has been translated into American English.

# Social Requirements

Please note that in order for this to be effective, the bot account should have a white person as a user icon and a name that sounds white or pro-Trump (eg, includes 'deplorable'). An icon of Trump holding the bible is included.

The bot MUST also have a few hundred followers or it may be counter-productive. To get followers, you may either purchase them or just let your bot run for a week or so and it will gradually build up a following on it's own. If you get impatient, you can login and try following some users on #MAGA or Trump-related hashtags or click on suggested accounts. Try to pick accounts that have a good ratio of following to followers.

If you are starting from a new account, follow all the initial
suggestions that Twitter gives you. Make a few tweets, including
the suggested 'First Tweet' that the Twitter website recommends.
Your first few manual tweets should either be innocuous or demonstrating membership of the pro-Trump or evangelical milieu.

# How it works

Once the bot has enough followers, every 5 hours, when someone tweets a tweet containing a certain trigger word or phrase, invandringsbot will reply with a callout.  If the bot responds too often, twitter will ban it, so the long wait is necessary.

In this specific, forked implementation of invandringsbot, the trigger word is "rapefugee" and the callout is about the moral responsibility we have to welcome refugees. However, the trigger word can be anything, as can the callout be. Both can be found in the setup file.

# Translate into your language/ take on another issue!

It's not only Swedes and xenophobes who are in need of a admonishment about our moral responsibilities. Make the world a better place by translating invandringsbot!

# Getting started:

You will need python and [Twython](https://github.com/ryanmcgrath/twython). Click for details on how to install.

1. Create (or repurpose) a twitter account. (See social requirements above).
2. Fork this repository.
3. Rename the `apikeys_template.py` file to `apikeys.py`, and add your Twitter API keys as obtained from apps.twitter.com.
4. If you wish to change the trigger word, the callouts, or general content the bot tweets, open `setup.py`
5. Now, start invandringsbot by calling `python mainbot.py`, when in the correct directory in your terminal.

# Dependencies

Using python 3. Must meet the requirements of Twython.

- [Twython](https://github.com/ryanmcgrath/twython). Used for all contact with the Twitter API.
