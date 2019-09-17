import googlemaps
import pprint
import time

#this is opening a file with the API key so this can be ignored 
keyFile = open("spartan.txt", "r")
#kFile is the API key 
kFile = keyFile.read()

#https://www.youtube.com/watch?v=qkSmuquMueA
#Set Google maps API Key
#This API key can be used for several API calls.  Geocoding, Geolocation, Places
#Client(*key = API_KEY)  *key = is needed 
gmaps_key = googlemaps.Client(key = kFile)

#Geocoding an address
geocode_result = gmaps_key.geocode('2079 Zumbehl Rd, St Charles, MO')
pprint.pprint(geocode_result)
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps_key.reverse_geocode((38.815615, -90.552195))
pprint.pprint(reverse_geocode_result)

#The following link is documentation to the places api 
#https://developers.google.com/places/web-service/intro

#Uses google places api to get the surrounding building of type in radius of XX meters
#https://developers.google.com/places/web-service/search
#https://developers.google.com/places/web-service/supported_types
places_result = gmaps_key.places_nearby(location = '38.885615, -90.532195', radius = 1000, open_now = False, type = 'restaurant') 

pprint.pprint(places_result)

#pause program of the page loads
#time.sleep(3)

#if there is not more than 20 results from the first search it will error out on this result
#places_result = gmaps_key.places_nearby(page_token = places_result['next_page_token']) 

#pprint.pprint(places_result)

for place in places_result['results']:
    
    #define place id
    my_place_id = place['place_id']
    
    #define fields we want sent back to us
    #https://developers.google.com/places/web-service/details
    my_fields = ['name', 'type', 'vicinity']
    
    #make a request for the details
    place_details = gmaps_key.place(place_id = my_place_id, fields = my_fields)
    
    pprint.pprint(place_details)

