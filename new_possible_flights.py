import json 
import os 

def add_new_flight_line(origin_airport,destination_airport):
    new_line = {}
    file_name = 'available_flights.json'
    if not os.path.exists(file_name):
            return "error. file does not exist"
    else:
        with open(file_name, 'r') as f:
            data = json.load(f)
        new_line = {
            "origin_airport": origin_airport,
            "destination_airport": destination_airport}
        data["available_lines"].append(new_line)

        with open(file_name, 'w') as f:
            json.dump(data, f)

        print(f"Flight line from {origin_airport} to {destination_airport} was added successfully!")

    
        
add_new_flight_line("TLV", "jlm")