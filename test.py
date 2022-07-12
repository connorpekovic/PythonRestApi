import requests
import json

contextDictionary = {}

# Get the weather in Chicago
endpoint = 'https://weatherdbi.herokuapp.com/data/weather/chicago'
responce = requests.get(endpoint) #GET request
data = responce.json() #JSON -> Python Dictionary
chicagoTemp = data['currentConditions']['temp']['f'] #Query data from dictionary

contextDictionary['chicagoTemp'] = chicagoTemp

#test
print('contextDictionary: ', contextDictionary)
    