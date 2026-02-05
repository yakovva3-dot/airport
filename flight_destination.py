import csv
import json
import pathlib

def select_destination():
    select = []
    
    with open('available_lines.json','r') as f:
        flights_available = json.load(f)
    print(flights_available)
    origin = input("Please enter the departure point of the flight of list: ")
    while origin not in flights_available:
        print("Error! The starting point was not found.")
        print(flights_available)
        origin = input("Please enter the departure point of the flight of list: ")
    select.append(origin)
    print(flights_available)
    destination = input("Please enter a flight destination of list: ")
    while destination not in flights_available:
        print("Error! The destination point was not found.")
        print(flights_available)
        destination = input("Please enter a flight destination of list: ")
    select.append(destination)
    return select
