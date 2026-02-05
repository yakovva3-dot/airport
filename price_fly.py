import csv
import json
import pathlib
import flight_destination

def price_of_flight():
    origin_destination = flight_destination.select_destination()
    continental_distance = []
    with open("airport_entry_fee.csv","r") as f:
        flight = list(csv.DictReader(f))
        for i in range(len(origin_destination)):
            for fly in flight:
                if origin_destination[i]==fly['airport_code']:
                    continental_distance.append(fly['continent'])
    with open("continents_pricing.csv","r") as f:
        price_calculation = csv.DictReader(f)
        for cost in price_calculation:
            if cost['source_continent']==continental_distance[0]:
                if cost['target_continent']==continental_distance[1]:
                    price = int(cost['base_price_usd'])/400+100
    return price


     
