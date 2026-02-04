def income_ticket_fair(money,budget_file):
    with open(budget_file,"r") as f:
        budget_before = int(f.read())
    budget_after = budget_before+money
    with open(budget_file,"w") as f:
        f.write(budget_after)
    return
    