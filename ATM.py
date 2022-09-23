# Python OOO CheatSheet: 
# https://www.w3schools.com/python/python_classes.asp

# Naive "ATM" that dispenses 50s, 20s, 10s which are all available
class ATM:

    # TODO
    _available_bills = None

    # Remember: in python all method signature receive a self as 1st param
    def withdraw(self, amount):
        
        # Basic input checks
        if not isinstance(amount, int):
            return -1

        if (amount <= 0):
            return -1

        # Number of 50s needed
        fifties = int(amount/50)
        
        # Number of 20s needed
        remainingAmount = amount-(fifties*50)
        twenties = int((remainingAmount)/20)

        # Number of 10s needed
        remainingAmount = remainingAmount-(twenties*20)
        tens = int(remainingAmount/10)

        return self.dispense(fifties, twenties, tens)

    def dispense(self, fifties, twenties, tens):
        return "£50x"+str(int(fifties))+" £20x"+str(int(twenties))+" £10x"+str(int(tens))

    def isInt(number):
        return isinstance(number, int)        

    def __init__(self, available_bills):
        self._available_bills = available_bills
