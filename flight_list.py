def print_flight_options(flight_dest_file):
    with open(flight_dest_file,"r") as f:
        document = f.readlines()
    return document