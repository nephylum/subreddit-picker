import praw
import pandas as pd
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM

reddit = praw.Reddit(client_id='Q7UNO346bOo_lg',
                     client_secret='ZbVhRrpo6nlHhXaq72FRIwCSizg',
                     user_agent='My user agent')

test = []

for submission in reddit.subreddit('starcitizen').hot(limit=3):
    print(submission.title)
    print(submission.selftext)
    # test.append(''.join(BeautifulSoup(submission.selftext, features="lxml").findAll(text=True)))
    # test.append(submission.selftext)
    print(submission.num_comments)
    # print(submission.comments[1])
    # for comment in submission.comments:
    #     print(comment.body)
    print('-----------')
# reddit.subreddits.search_by_topic('space')

# reddit.subreddit('starcitizen').hot(limit=1).selftext
print('**********')
# for it in test:
#  print (''.join(BeautifulSoup(it, features="lxml").findAll(text=True)))

data = pd.DataFrame()
top200 = ["AdviceAnimals","AmItheAsshole","Android","AnimalsBeingBros",
"AnimalsBeingDerps","AnimalsBeingJerks","Art","ArtisanVideos","AskMen",
"AskReddit","Awwducational","BeAmazed","BetterEveryLoop","BikiniBottomTwitter",
"BlackPeopleTwitter","ChildrenFallingOver","ChoosingBeggars",
"ContagiousLaughter","Cooking","CrappyDesign","DIY","Damnthatsinteresting",
"DnD","Documentaries","EarthPorn","EatCheapAndHealthy","Eyebleach","FiftyFifty",
"Fitness","FoodPorn","Futurology","Games","GetMotivated","GifRecipes",
"HighQualityGifs","HistoryMemes","HistoryPorn","HumansBeingBros","IAmA",
"IdiotsInCars","InternetIsBeautiful","Jokes","KidsAreFuckingStupid",
"LifeProTips","MadeMeSmile","MakeupAddiction","Minecraft","MovieDetails",
"MurderedByWords","Music","NSFW_GIF","NatureIsFuckingLit","NetflixBestOf",
"NintendoSwitch","NoStupidQuestions","OldSchoolCool","OutOfTheLoop","Outdoors",
"Overwatch","PS4","Parenting","PewdiepieSubmissions","PublicFreakout",
"RealGirls","Roadcam","RoastMe","Showerthoughts","StarWars","Tinder",
"TrendingReddits","TrollYChromosome","TwoXChromosomes","Unexpected",
"UpliftingNews","WTF","WatchPeopleDieInside","Wellthatsucks","Whatcouldgowrong",
"WhitePeopleTwitter","WritingPrompts","YouShouldKnow","anime","announcements",
"askscience","atheism","aww","backpacking","battlestations","bestof","biology",
"blackmagicfuckery","blog","boardgames","books","buildapc","cars","cats",
"confession","creepy","cursedcomments","dadjokes","dankmemes","dataisbeautiful",
"drawing","electronicmusic","europe","explainlikeimfive","facepalm","food",
"frugalmalefashion","funny","gadgets","gameofthrones","gaming","gardening",
"gifs","gonewild","hiphopheads","history","hmmm","horror","howto","humor",
"insanepeoplefacebook","instant_regret","interestingasfuck","iphone",
"itookapicture","keto","leagueoflegends","lifehacks","listentothis","loseit",
"mac","madlads","malefashionadvice","me_irl","memes","mildlyinfuriating",
"mildlyinteresting","movies","natureismetal","nba","nevertellmetheodds","news",
"nextfuckinglevel","nfl","nintendo","nonononoyes","nosleep","nottheonion",
"nsfw","oddlysatisfying","offmychest","pcgaming","pcmasterrace",
"personalfinance","philosophy","photography","photoshopbattles","pics",
"pokemon","pokemongo","politics","programming","rarepuppers","raspberry_pi",
"reactiongifs","reallifedoodles","recipes","relationship_advice",
"relationships","rickandmorty","science","scifi","sex","slowcooking","soccer",
"socialskills","space","sports","streetwear","tattoos","technology","teenagers",
"television","therewasanattempt","tifu","todayilearned","trashy","travel",
"trees","trippinthroughtime","videos","whatisthisthing","wholesomememes",
"woahdude","woodworking","worldnews","xboxone","youseeingthisshit"]
# sub_name = ["starcitizen", "AmItheAsshole"]

for sub in top200:
    comments = []
    # data[sub] = []
    for submission in reddit.subreddit(sub).hot(limit=300):
        comments.append(submission.title)
        comments.append(submission.selftext)
    print('comment length:', len(comments))
    data[sub] = comments
    # data[sub].append(comments, ignore_index=True)
for s in data:
    print(data[sub_name])
    print(len(data))
data.to_csv('test.csv')
