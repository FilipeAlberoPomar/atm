

# https://www.w3schools.com/python/python_classes.asp

class ATM:

    _available_bills = None

    # Remember: in python all method signature receive a self as 1st param
    def withdraw(self, amount):
        print("withdraw")
        return 0

    def __init__(self, available_bills):
        print("constructor")
        self._available_bills = available_bills
