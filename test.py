import praw
import pandas as pd
import datetime as dt 
from praw.models import MoreComments
import operator

reddit = praw.Reddit(client_id='Client id', \
                     client_secret='CLient secret', \
                     user_agent='Scraper', \
                     username='Username', \
                     password='Password')

subreddit = reddit.subreddit('cscareerquestions')

top_subbreddit = subreddit.top()
count = 0
max = 5000
print('success')
words = []
wordCount = {}
commonWords = {'that','this','and','of','the','for','I','it','has','in',
'you','to','was','but','have','they','a','is','','be','on','are','an','or',
'at','as','do','if','your','not','can','my','their','them','they','with',
'at','about','would','like','there','You','from'}

for submission in subreddit.top(limit=50):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        count += 1
        if(count == max):
            break
        # print(top_level_comment.body)
        word = ""
        for letter in top_level_comment.body:
            if(letter == ' '):
                if(word and not word[-1].isalnum()):
                    word = word[:-1]
                if not word in commonWords:
                    words.append(word)
                
                word = ""
            else:
                word += letter
            # print(letter)
    if(count == max):
            break

print(count)

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1
    # print(word)

print(len(words))

sortedList = sorted(wordCount.items(), key=operator.itemgetter(1))

for entry in sortedList:
    print(entry)

