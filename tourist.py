# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:06:58 2020

@author: bhavy
"""
destinations=["Paris,France","Shanghai,China","Los Angeles,USA","Sao Paulo, Brazil", "Cairo,Egypt"]
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

attractions=[[],[],[],[],[]]
def add_attractions(destination,attraction):
  d_i=get_destination_index(destination)
  a_f_d=attractions[d_i]
  a_f_d.append(attraction)
  return
add_attractions("Los Angeles,USA",["Venice Beach", ["beach "]])
add_attractions("Paris,France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris,France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Shanghai,China", ["Yu Garden", ["garden", "historcical site"]])
add_attractions("Shanghai,China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai,China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles,USA", ["LACMA", ["art", "museum"]])
add_attractions("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attractions("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attractions("Cairo,Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo,Egypt", ["Egyptian Museum", ["museum"]])
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
la_arts=find_attractions("Los Angeles,USA",["art"]) 
print(la_arts)