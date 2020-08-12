from flask import Flask, request, redirect, url_for, flash, jsonify, render_template

import json

import requests




tourist_app = Flask(__name__)

destinations=["Paris,France","Shanghai,China","Los Angeles,USA","Sao Paulo, Brazil", "Cairo,Egypt","New York,USA", "London,UK"]
test_traveler= ["Erin Wilkes", "Shanghai,China", ["historical site", "art"]]

def get_destination_index(destination):
  destination_index=destinations.index(destination)
  return destination_index
print(get_destination_index("Los Angeles,USA"))
print(get_destination_index("Paris,France"))
def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]   
  traveler_destination_index=get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index=(get_traveler_location(test_traveler))
print(test_destination_index)

attractions=[[],[],[],[],[],[],[]]
def add_attractions(destination,attraction):
  d_i=get_destination_index(destination)
  a_f_d=attractions[d_i]
  a_f_d.append(attraction)
  return
add_attractions("Los Angeles,USA",["Venice Beach", ["beach"]])
add_attractions("Los Angeles,USA", ["LACMA: Los Angeles County Museum of Art", ["art", "museum"]])
add_attractions("Los Angeles,USA", ["Huntington Library and Botanical Gardens", ["garden"]])
add_attractions("Los Angeles,USA", ["Hollywood Sign", ["monument"]])
add_attractions("Los Angeles,USA", ["Greystone Mansion", ["historical site"]])
add_attractions("Los Angeles,USA", ["Wilshire Grand Center", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles,USA", ["Los Angeles Zoo", ["zoo"]])


add_attractions("Paris,France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris,France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Paris,France", ["Eiffel Tower", ["historical site", "monument", "viewing deck"]])
add_attractions("Paris,France", ["Deauville Beach", ["beach"]])
add_attractions("Paris,France", ["Jardin des Tuileries", ["garden"]])
add_attractions("Paris,France", ["Paris Zoological Park", ["zoo"]])
add_attractions("Paris,France", ["Tour Montparnasse", ["skyscraper", "viewing deck"]])





add_attractions("Shanghai,China", ["Yu Garden", ["garden", "historical site"]])
add_attractions("Shanghai,China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai,China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Shanghai,China", ["Jinshan City Sand Beach", ["beach"]])
add_attractions("Shanghai,China", ["The Bund (Wai Tan)", ["monument"]])
add_attractions("Shanghai,China", ["Shanghai Zoo", ["zoo"]])


add_attractions("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attractions("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attractions("Sao Paulo, Brazil", ["Edifício Itália", ["skyscraper", "viewing deck"]])
add_attractions("Sao Paulo, Brazil", ["São Paulo Brazil Temple", ["monument"]])
add_attractions("Sao Paulo, Brazil", ["Santos City Beach", ["beach"]])
add_attractions("Sao Paulo, Brazil", ["Jardim Botânico de São Paulo", ["garden"]])
add_attractions("Sao Paulo, Brazil", ["São Paulo Museum of Art", ["art", "museum"]])



add_attractions("Cairo,Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo,Egypt", ["Egyptian Museum", ["museum", "art"]])
add_attractions("Cairo,Egypt", ["Ras Abu Galoum, Dahab", ["beach"]])
add_attractions("Cairo,Egypt", ["The Cairo Tower", ["skyscraper", "viewing deck"]])
add_attractions("Cairo,Egypt", ["Giza Zoo", ["zoo"]])
add_attractions("Cairo,Egypt", ["Orman Garden", ["garden"]])

add_attractions("New York,USA", ["Statue of Liberty", ["monument", "historical site"]])
add_attractions("New York,USA", ["The National 9/11 Memorial and Museum", ["monument", "historical site"]])
add_attractions("New York,USA", ["The Metropolitan Museum of Art", ["museum", "art"]])
add_attractions("New York,USA", ["MOMA: The Museum of Modern Art", ["museum", "art"]])
add_attractions("New York,USA", ["American Museum of Natural History", ["museum"]])
add_attractions("New York,USA", ["Coney Island Beach", ["beach"]])
add_attractions("New York,USA", ["The Empire State Building", ["skyscraper", "viewing deck"]])
add_attractions("New York,USA", ["One World Trade Center", ["skyscraper"]])
add_attractions("New York,USA", ["Top of the Rock, Rockfeller Center", ["viewing deck"]])
add_attractions("New York,USA", ["Bronx Zoo", ["zoo"]])
add_attractions("New York,USA", ["Central Park", ["garden"]])

add_attractions("London,UK", ["Westminster Palace", ["monument", "historical site"]])
add_attractions("London,UK", ["Tower Bridge", ["monument", "historical site"]])
add_attractions("London,UK", ["Big Ben", ["monument", "historical site"]])
add_attractions("London,UK", ["Buckingham Palace", ["monument", "historical site"]])
add_attractions("London,UK", ["National Gallery", ["museum", "art"]])
add_attractions("London,UK", ["British Museum", ["museum", "art"]])
add_attractions("London,UK", ["Natural History Museum", ["museum"]])
add_attractions("London,UK", ["Camber Sands, East Sussex", ["beach"]])
add_attractions("London,UK", ["Tower Bridge", ["viewing deck"]])
add_attractions("London,UK", ["One Shard", ["skyscraper", "viewing deck"]])
add_attractions("London,UK", ["London Eye", ["viewing deck"]])
add_attractions("London,UK", ["Sky Garden", ["viewing deck"]])
add_attractions("London,UK", ["London Zoo", ["zoo"]])
add_attractions("London,UK", ["Hyde Park", ["garden"]])
add_attractions("London,UK", ["Royal Botanical Gardens, Kew", ["garden"]])




def find_attractions(destination,interests):
  d_i=get_destination_index(destination)
  attractions_in_city=attractions[d_i]
  attractions_with_interest=[]
  for attraction in attractions_in_city:
    possible_attraction=[attraction]
    possible_attraction.append(attraction)
    attractions_tags=attraction[1]
    for interest in interests:
     if interest in attractions_tags:
       attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest


    

#################APP ROUTES####################

@app.route('/')
def home():
    return render_template('index.html')

#################################################

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        req = request.form
        destination = req["Destination"]
        interests = req["Interests"]
        output = find_attractions(destination, [interests])

    

        
    return render_template('index.html', prediction_text='Our recommendation for your selection is =  {}'.format(output))




if __name__ == "__main__":
    tourist_app.run(debug=True)
