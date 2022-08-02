import unittest

from ATM import ATM

# https://docs.python.org/3/library/unittest.html

class TestATM(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        available_bills = {}
        available_bills = [5, 0]
        available_bills = [10, 0]
        available_bills = [20, 0]
        available_bills = [50, 0]
        self.atm = ATM(available_bills)

    def test_five(self):
        atm.withdraw(5)
        self.assertEqual(self.atm.withdraw(5), 5)


if __name__ == '__main__':
    unittest.main()