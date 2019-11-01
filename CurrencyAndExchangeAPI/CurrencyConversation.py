import pprint
import json
import urllib.request  #library used for opening urls 

#https://www.exchangerate-api.com/
currency = 'USD'

test = f'https://api.exchangerate-api.com/v4/latest/{currency}'

jsonURL = urllib.request.urlopen(test)
data = json.loads(jsonURL.read())

#pprint.pprint(test)


pprint.pprint(data)