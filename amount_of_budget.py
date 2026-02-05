# input budget.txt output a number
def amount in budget():
    with open ("budget.txt", "r") as f:
        amount = int(f.readline())
    return amount

