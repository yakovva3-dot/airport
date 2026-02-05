import csv
import json
import pathlib

def select_destination():
    with open('available_lines.json','r') as f:
        flights_available = json.load(f)
    print(flights_available)
    origin_destination = input("Please enter a starting point and a destination point from the list: ")
    while origin not in flights_available:
        print("Error! The line does not exist in the system.")
        print(flights_available)
        origin_destination = input("Please enter a starting point and a destination point from the list: ")
    select = flights_available[origin_destination]
    
    return select
