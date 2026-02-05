def passenger_or_ceo():
    while True:
        try:
            answer = int(input("are you a passenger or the ceo. if you are a passenger please press 1. if you are the ceo press 2"))
            if answer != 1 and answer != 2:
                raise ValueError
            break
        except ValueError:
            print("choose either 1 or 2 please")
    if answer == 1:
        return "passenger"
    else:
        return "ceo"