import pprint
import json
import urllib.request  #library used for opening urls 

#this is opening a file with the API key so this can be ignored 
keyFile = open("YepYep.txt", "r")
#The API key 
apiKey = keyFile.read()

#https://www.alphavantage.co/documentation/
timeSeries = 'TIME_SERIES_DAILY'

#Microsoft ticker symbol
ticker = 'MSFT'

#url to modify to open the link for the json data
url = f'https://www.alphavantage.co/query?function={timeSeries}&symbol={ticker}&apikey={apiKey}'

jsonURL = urllib.request.urlopen(url)
data = json.loads(jsonURL.read())

pprint.pprint(data)