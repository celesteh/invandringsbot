import random
# This file contains the rant array, the screen name of the user, and the trigger word

# The Twitter handle of the bot.
screen_name = "GrateAmerica"

# Each word that contains any of these trigger words will be replied to.
# Note that indicated sarcastic uses of the word (in quotes) will trigger a rant.
# Each trigger word should be separated by a comma, without a space.
# Don't use too many or too broad words, as that will generate too many tweets.
trigger_words = "rapefugee,rapefugees"

# The rant to reply to each user that has tweeted the trigger word with.
# No more than 15 tweets are allowed, due to the rate limits of the Twitter API.
rant = [#"Hey, that kind of talk hurts real people. Remember, Jesus was a refugee in Egypt. #MAGA",
        #"Hey, that kind of talk hurts real people. My grate grandparents were refugees from Ireland. #MAGA",
        "Hey, that kind of talk hurts real people. Leviticus 19:33-34 commands us to take refugees.",
        "Hey, that kind of talk hurts real people. Matthew 25:35 commands us welcome strangers. #MAGA",
        "Hey, that kind of talk hurts real people. They used to say the same things abt Catholics, like VP Pence. #MAGA",
        "That's a racist and gross thing to say, which hurts real people. You should stop."]

def make_reply():
    return random.choice(['Leviticus 19:33-34 and Matthew 25:35', 'Matthew 25:35 and Leviticus 19:33-34'])+random.choice([" command", " tell", " instruct"])+ " us to " +random.choice(['welcome strangers', 'welcome refugees', 'accept refugees', 'take refugees']) + ". " + random.choice(["I'll pray", "I'm praying"])  + ' for you.'

non_reply = random.choice(["Today ", "This morning ", "This afternoon ", "At church ", "In bible study ", "Tuesday ", "On Sunday ", "Next week ", ""]) + "I'm " + random.choice(["remembering ", "praying for ", "saying a prayer for ", "lighting a candle for ", "honering ", "asking for God's blessings on ", "asking Jesus to bless ", "asking God to sanctify ", "leading a prayer for "]) + random.choice(["veterans. ", "our soliders. ", "POWs. ", "those who died for US. ", "the gratest generation. ", "WWII vets. ", "victims of terrism. ", "my grandfather. "]) + random.choice(["#MAGA", "#PrayForAmerica", "#PrayForVetrans", "#GodBlessAmerica", "@RealDonaldTrump", '#TrumpTrain'])

templates = [
[["Today ", "This morning ", "This afternoon ", "At church ", "In bible study ", "Tuesday ", "On Sunday ", "Next week ", ""], "I'm ", ["remembering ", "praying for ", "saying a prayer for ", "lighting a candle for ", "honering ", "asking for God's blessings on ", "asking Jesus to bless ", "asking God to sanctify ", "leading a prayer for "], ["veterans. ", "our soliders. ", "POWs. ", "those who died for US. ", "the gratest generation. ", "WWII vets. ", "victims of terrism. ", "my grandfather. "],["#MAGA", "#PrayForAmerica", "#PrayForVetrans", "#GodBlessAmerica", "@RealDonaldTrump", '#TrumpTrain']],
[['Making America Grate Again ', 'Prayer ', 'Family ', 'Jesus ', 'Providing for my children '], "is what ", ['gives me purpose.', 'gives my life meaning.', 'gets me up in the morning.', 'gives me joy.', 'brings me happiness.', 'brings love to my life.', 'brings light to my life.', 'keeps me going.', 'brings joy to my heart.', 'makes my world go round.']],
[['My dog', 'My cat'],' ', ["wants out when it's in and in when it's out", 'could stand to be more housebroken.', 'is the cutest thing ever.', 'is always by my side.', 'should be a social media star.', 'will not be quiet!', "ate my kid's homework! lol!! (writing a note now.)", 'is almost too fluffy.', 'always wants attention.', "is always in my wife's lap whenver she sits down.", 'will not stop begging.', 'prefers the cheaper food.', 'does not act like the ones in TV commercials!', 'is at it again.', 'has not gotten less destrictive with age.', 'makes a rediculous racket.', 'ate another houseplant.', 'is a menace to squirrels.', 'is eating grass again. uhoh.', 'heard me say V-E-T and is hiding somewhere.', 'has seen a bird through the window.', 'is carrying on for some reason.', 'will not stop running around the house.', 'is the background image on my phone.', 'has ruined my curtains.', 'has ruined my carpet.', 'is being sick.', 'is silly.', 'is rediculous.', 'ran away once, but came home.'], ' ', ['#lovePets', '#PetLife', '#FurryFriends', '#FuzzyFace', '', '', '', '']]
]

# The last 4 accounts here are related to US sports
# You can/should replace them with different sports teams
accounts_to_rt = ['CuteEmergency', 'AChristLife', 'EmrgencyKittens', 'AllGreatAgain', 'Vol_Football', 'Titans',  'okcthunder', 'UpTheThunder']
