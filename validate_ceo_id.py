import csv

def validate_ceo_id(user_input,pass_input,crdetials_file):
    with open(crdetials_file,"r") as f:
        csv_obj = csv.reader(f)
        header = next(csv_obj)
        for row in csv_obj:
            user,passw = row
            if user == user_input and passw == pass_input:
                return True
        return False