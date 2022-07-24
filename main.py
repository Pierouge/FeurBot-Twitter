import twitter
import time
import os
import sys

api = twitter.Api(consumer_key='Your consumer key',
                  consumer_secret='Your consumer secret key',
                  access_token_key='Your access token key',
                  access_token_secret='Your access token secret key')
global feurwords
feurwords = ["quoi", "koi", "coi", "qoua", "quoua", "koua",
             "kwa", "qwa", "cwa", "qoi", "koa", "cua", "kua"]
global feurlist
feurlist = os.listdir("feur")
global deletethis
deletethis = ["xd", "x)", ":d", ":p", " "]
global emoji_pattern
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002500-\U00002BEF"  # chinese char
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           "]+", flags=re.UNICODE)

def rate_limit():
    print("Limite atteinte, on dort 15 minutes")
    rate_limiter = 0
    time.sleep(15*60)
    YES()

def YES():
    tweets = 0
    recherches = 0
    id = 0
    routines = 1
    rate_limiter = 0
    while True:
        print("Lancement de la routine numéro " + str(routines))
        recherches = 0
        if rate_limiter < 14:
            rate_limiter += 1
            for search in api.GetSearch(term='quoi', lang='fr', result_type='recent', since_id=id, count=100):
                recherches += 1
                print("On a déjà effectué "+str(recherches)+" recherches !")
                feurmessage = str(message.content).lower()
                feurmessage = re.sub('[!-?]', '', feurmessage)
                feurmessage = re.sub('http\S+', '', feurmessage)
                feurmessage = re.sub('@\S+', '', feurmessage)
                feurmessage = emoji_pattern.sub('', feurmessage)
                feurmessage = feurmessage.replace(" ", "")
                feurmessage = re.sub('[^a-zA-Z]', '', feurmessage)
                for i in deletethis:
                    if i in str(message.content).lower():
                        feurmessage = feurmessage.replace(i, "")
                for j in feurwords:
                    if feurmessage.endswith(j):
                        if tweets == 0:
                            id = search.id
                        if rate_limiter < 14:
                            api.PostUpdate("@" + search.user.screen_name, in_reply_to_status_id=search.id, media="feur/"+feurlist[random.randint(0, len(feurlist)-1)])
                            tweets += 1
                            rate_limiter += 1
                            print("On a déjà tweeté "+str(tweets)+" fois !")
                            time.sleep(10)
                        else:
                            rate_limit()
                            return
                        break
            routines += 1
        else :
            rate_limit()
        time.sleep(10)

YES()

