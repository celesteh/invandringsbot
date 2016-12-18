import random
# This file contains the callout array, the trigger word,
# the templates for normal tweets, the accounts to RT,
# and the percentage of retweets vs generated tweets


# if you've recently had your account warned about
# suspicious activity, set this to True for a while
on_probation = False
#on_probation = True


# Each word that contains any of these trigger words will be replied to.
# Note that indicated sarcastic uses of the word (in quotes) will trigger a rant.
# Each trigger word should be separated by a comma, without a space.
# Don't use too many or too broad words, as that will generate too many tweets.
trigger_words = "rapefugee,rapefugees"

# The rant to reply to each user that has tweeted the trigger word with.
# No more than 15 tweets are allowed, due to the rate limits of the Twitter API.
callouts = [
["Hey, using slurs like that hurts real people. Leviticus 19:33-34 ", ['commands us to take', 'tells us to welcome'], " refugees.", [" #MAGA", ""]],
["Hey, using slurs like that hurts real people. Matthew 25:35 ", ['commands us to take', 'tells us to welcome'], " refugees.", [" #MAGA", ""]],
["Hey, using slurs like that hurts real people. They used to say the same things abt Catholics, like VP Pence.", [ " #MAGA", ""]],
["That's a ", ['racist and gross', 'gross and racist'], " slur, which hurts real people. You should stop."]#,
#[['Leviticus 19:33-34 and Matthew 25:35', 'Matthew 25:35 and Leviticus 19:33-34'],[" command", " tell", " instruct"], " us to ", ['welcome strangers', 'welcome refugees', 'accept refugees', 'take refugees'], ". ", ["I'll pray", "I'm praying"], ' for you.', [ " #MAGA", ""]]
]


templates = [
[["Today ", "This morning ", "This afternoon ", "At church ", "In bible study ", "Tomorrow ", "This Sunday ", "Next week ", ""], "I'm ", ["remembering ", "praying for ", "saying a prayer for ", "lighting a candle for ", "honoring ", "asking for God's blessings on ", "asking Jesus to bless ", "asking God to sanctify ", "leading a prayer for "], ["veterans. ", "our soliders. ", "POWs. ", "those who died for US. ", "the greatst generation. ", "WWII vets. ", "victims of terrorism. ", "my grandfather. "],["#MAGA", "#PrayForAmerica", "#PrayForVetrans", "#GodBlessAmerica", "@RealDonaldTrump", '#TrumpTrain', '#tcot']],
[['I always say, ', 'Like I say, ', 'As I tell my wife, ', 'Once again, I repeat, ', 'As I like to say, ', "I'm like a broken record with this: ", "I'll say it again: ", '', '', '', ''], ['Making America Great Again ', 'Prayer ', 'Family ', 'Jesus ', 'Providing for my children '], ["is what ", 'always ', ''], ['gives me purpose.', 'gives my life meaning.', 'gets me up in the morning.', 'gives me joy.', 'gives me hope', 'brings me happiness.', 'brings love to my life.', 'brings light to my life.', 'keeps me going.', 'brings joy to my heart.', 'makes my world go round.']],
[['My dog', 'My cat', 'The dog','The cat'],' ', ["wants out when it's in and in when it's out", 'could stand to be more housebroken.', 'is the cutest thing ever.', 'is always by my side.', 'should be a social media star.', 'will not be quiet!', "ate my kid's homework! lol!! (writing a note now.)", 'is almost too fluffy.', 'always wants attention.', "is always in my wife's lap whenver she sits down.", 'will not stop begging.', 'prefers the cheaper food.', 'does not act like the ones in TV commercials!', 'is at it again.', 'has not gotten less destrictive with age.', 'is making a rediculous racket.', 'ate another houseplant.', 'is a menace to squirrels.', 'is eating grass again. uhoh.', 'heard me say V-E-T and is hiding somewhere.', 'has seen a bird through the window.', 'is carrying on for some reason.', 'will not stop running around the house.', 'is the background image on my phone.', 'has ruined my curtains.', 'has ruined my carpet.', 'is being sick.', 'is silly.', 'is rediculous.', 'ran away once, but came home.', 'has learned to mash his face into my keyboard when he wants attention.', 'is really cute but also really dumm.', 'knocked over the Christmas tree last year!', 'keeps licking his tail until he leaves a wet spot on the sofa. yuck.', 'is eager to "make friends with" the kids guinea pig. #NotAGoodIdea', 'was a rescue. I adopted him from the shelter when he was 9 weeks old. So glad I did!'], ' ', ['#lovePets', '#PetLife', '#FurryFriends', '#FuzzyFace', '', '', '', '']],
[['We', 'America'], ' must ', ['always remember', 'never forget', 'always honer', 'always honor', 'always pray for', 'pray for', 'ask God to bless', 'thank God for', 'hold in our hearts', 'always respect'], [' the sacrifices of ', ' ', ' '], ['our parents.', 'our grandparents.', 'firefighters.', 'veterans.', 'vetrans.', 'those who served.', '9/11 first responders.'], ' ', ['#MAGA', '#PrayForAmerica', '#GodBlessAmerica', '#TrumpTrain', '#PrayerTrain', '', ''], [' #ProtectTheirHealthCare', '', '']],
[['God ', 'The Lord ', 'The Bible '], ['commands: ', 'demands: ', 'instructs us: ', 'says: ', 'tell us: '], ['I am the LORD your God: you shall have no other Gods before me', "You shall not take the Lord's name in vain.", "Remember to keep holy the LORD'S Day holy.", 'Honor your father and your mother.', 'You shall not bear false witness against your neighbor.', "You shall not covet your neighbor's wife.", "You shall not covet your neighbour's goods.", 'trust in Him. Psalm 23:1 The LORD is my Shepherd; I shall not want.', 'Love God above all things.', 'Love your neighbour as yourself.'], ' ', ['#RememberGod', '#ObeyGod', '#GodsLaw', '#Commandment', '#1NationUnderGod', '#GodBlessAmerica', '', '', '']]
]

# The last 4 accounts here are related to US sports
# You can/should replace them with different sports teams
accounts_to_rt = ['CuteEmergency', 'AChristLife', 'EmrgencyKittens', 'AllGreatAgain', 'USNHistory', 'JenaC2', 'Vol_Football', 'Titans',  'okcthunder', 'UpTheThunder']

# What percentage should be retweets vs original content?
# Number between 0-1
percent_rt = 0.65
