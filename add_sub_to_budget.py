def income_outgoing_budget(money,budget_file,func):
    money = int(money)
    with open(budget_file,"r") as f:
        budget_before = f.read()
        budget_before = int(budget_before)
        if func == "+":
            budget_after = money + budget_before
        else:
            budget_after = money - budget_before
            if budget_after > 0:
                budget_after = str(budget_after)
                with open(budget_file,"w") as f:
                    f.write(budget_after)
            return "cannot purchase, since not enough money in budget"
    return
