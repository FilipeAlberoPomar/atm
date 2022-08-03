# Python OOO CheatSheet: 
# https://www.w3schools.com/python/python_classes.asp

# Naive "ATM" that only dispenses unlimited 10 and 20 bills
class ATM:

    # TODO cater for available bills
    _available_bills = None

    # Remember: in python all method signature receive a self as 1st param
    def withdraw(self, amount):
        
        if not isinstance(amount, int):
            return -1

        intAmount = int(amount)
        if (intAmount <= 0):
            return -1

        notes20 = intAmount / 20
        notes10 = (intAmount % 20) / 10

        return_value = "£20x"+str(int(notes20))+" £10x"+str(int(notes10))

        return return_value


    def __init__(self, available_bills):
        self._available_bills = available_bills
