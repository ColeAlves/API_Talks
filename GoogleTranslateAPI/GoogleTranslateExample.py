#Imports the Google Cloud client library
from google.cloud import translate

#https://cloud.google.com/docs/authentication/getting-started

#https://www.youtube.com/watch?v=WH7EQFbuIrI
#Do not put the json file in a github respository 
#Instantiates a client
translate_client = translate.Client()

#The text to translate
text = u'Guten Tag'
#The target language
#English
target = 'eng'

#Translates some text into Russian
translation = translate_client.translate(text, target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))