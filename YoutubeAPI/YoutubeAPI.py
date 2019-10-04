import json
import urllib.request  #library used for opening urls 
import pprint

from pytube import YouTube

#this is opening a file with the API key so this can be ignored 
keyFile = open("EweTube.txt", "r")
#The API key 
apiKey = keyFile.read()

#https://developers.google.com/youtube/v3/quickstart/python

#videoID is the last several characters in the youtube link
videoID = "MHS-htjGgSY"

#f in prefix is a f-string or formatted string
url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={videoID}&key={apiKey}"

#opens the url link been given
jsonURL = urllib.request.urlopen(url)
data = json.loads(jsonURL.read())


pprint.pprint(data)

#class to get the id from the youtube link
class Helper:
    def id_from_url(self, url: str):
        #rsplit() method returns a list of strings after breaking 
        #the given string from right side by the specified separator
        #https://www.geeksforgeeks.org/python-string-rsplit/
        return url.rsplit("=", 1)[1]
    
s = "https://www.youtube.com/watch?v=TUcO-wHldaU"    
helper = Helper()
print(helper.id_from_url(s))