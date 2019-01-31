"""

PIRATE SPEAK TRANSLATOR
WRITTEN BY - SAMUEL EPODOI
API USED - https://funtranslations.com

!!!PLEASE NOTE THAT THIS ONLY WORKS ON PYTHON 3 AND ABOVE!!!

"""
#Import Required Libraries
import urllib.parse
import requests

#Pirate Api URL
api_url = 'https://api.funtranslations.com/translate/pirate.json?'

#Print credits
print ("\nPIRATE SPEAK TRANSLATOR \nWRITTEN BY - SAM EPODOI 💕 \nAPI USED - https://funtranslations.com \n")


#Execute and if RPH(REQUESTS per Hour) exceeded print error message
try :

  #User Text Input
  def repeat():
    english_text = input("What Text do you want to translate to pirate 😊 ? ")

    url = api_url + urllib.parse.urlencode({'text': english_text})
    json_data = requests.get(url).json()
    translated_text = json_data['contents']['translated'] 

    #Print Translated Text
    if english_text:
      print ("\n======================================\n")
      print('Translated Text: ' + translated_text)
      print ("\n======================================\n")

  while True:
    repeat()
    
  
except Exception as e: 
  print ("\n======================================\n")
  print("Awww snapp😢 \nMaximum number of requests!!! \nPlease try again in an hour")
  print ("\n======================================\n")






