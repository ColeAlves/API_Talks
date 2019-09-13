import praw #pip install praw
import os
import re
import cv2  #pip install opencv-python
import time  #to delay the program so it does not make too many requests
import numpy as np
import requests
from imgurpython import ImgurClient  #pip install imgur-uploader  


#https://www.youtube.com/watch?v=wAN8b38U_8c
#need to find the praw.ini and change it so this is not showing in github
reddit = praw.Reddit(client_id = '',
                    client_secret = '',
                    username = '',
                    password = '',
                    user_agent = 'GrayScale by /u/ColeAlves_M')

#use this line of code if you got the the praw.ini working
#reddit = praw.Reddit('grayscale', user_agent = 'GrayScale by /u/ColeAlves_M')

#imgur client to login and post stuff to imgur
#for posting the image on imgur  
client = ImgurClient('', '')

#the subreddit that the bot is currently active in
#this can be made into a list for multiple subreddits and you can loop through the list
subreddit = reddit.subreddit('testingground4bots')

#called upon by this phrase in the subreddit
#not used in this program but can be implemented later if search through comments
keyphrase = '!grayscale'

#Have this code ran before? If not, create an empty list
#This will create a file
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    #Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as fil:
        posts_replied_to = fil.read()
        posts_replied_to = posts_replied_to.split("\n")
        #https://www.programiz.com/python-programming/methods/built-in/filter
        #filter() method constructs an iterator from elements of an iterable for which a funct returns true
        #test each element in the iterable to be true or not
        #If None, the funct defaults to Identity funct. Returns false if any elements are false
        posts_replied_to = list(filter(None, posts_replied_to))


#Check the newest submissions in the subreddit and perform an operation on each submission
#The limit is how many posts to look at the given time of the program 50 or 100 should be fine
for submission in subreddit.new(limit = 50):
    
    #If the bot has not replied to this post before
    if submission.id not in posts_replied_to:
        #Case insensitive search
        #searches for a specific title post.
        if re.search("Hollow Citadal", submission.title, re.IGNORECASE):
            #submission.reply("This is a working reply Bot")
            print(submission.url)
            
            #Downloads the image from the post and labels it as test.jpg
            #After downloading then apply filters to the downloaded image then upload it to imgur
            with open('test.jpg', 'wb') as test:
                test.write(requests.get(submission.url).content)
            
            #Read the downloaded image
            img = cv2.imread('test.jpg')
            #print(img)
            
            #Apply the filter to make the image grayscale using the cvtColor function from cv2
            grayScaleOne = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('test.jpg', grayScaleOne)
            #confirming that the bot responded to the correct submission for testing
            #print("Bot replying to : ", submission.title)
            #print(submission.url)
            
            #Resize the window so the image can be seen better since there is a scaling issue with imshow
            #imS = cv2.resize(grayScaleOne, (900, 900))
            #cv2.imshow('Image', imS)
            #cv2.waitKey(0)
            #cv2.destoryAllWindows()#this is not working at all
            
            #uploads the the image into the variable image
            image = client.upload_from_path('test.jpg')

            #gets the link of the image that has been uploaded to imgur
            imageImgur = format(image['link'])
            print(imageImgur)
            
            #you can use the .reply() to reply to comments or posts
            #in this case a post
            submission.reply("The Hippogrith is landing!")
            
            #Put the submission id into a list of submissions that the bot replied too
            #This prevents spamming of a post and 
            posts_replied_to.append(submission.id)

            #Delays the program so when it is automated so that the bot does not reach the request limit set by the site
            #time.sleep(10)
            
#Add the submissions id from the list into the posts_replied_to file
with open("posts_replied_to.txt", "w") as fil:
    for post_id in posts_replied_to:
        fil.write(post_id + "\n")
        
#Delays the program so when it is automated so that the bot does not reach the request limit set by the site
#time.sleep(10)

#removes the image after it is posted to save space
#since the path is not given it deletes the file with the same name where the code file is
#try:
#    os.remove("test.jpg")
#except: pass