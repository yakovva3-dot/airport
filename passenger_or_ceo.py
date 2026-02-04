def pass_or_ceo():
    while True:
        try:
            answer = int(input("Are you a passenger or a CEO. if You Are a Passenger please press 1, if you are a CEO please enter 2: "))
            if answer != 1 and answer != 2:
                raise ValueError
            return answer
        except ValueError:
            print("please choose either 1 or two")
            