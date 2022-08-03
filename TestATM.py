import unittest
from ATM import ATM

# https://docs.python.org/3/library/unittest.html

class TestATM(unittest.TestCase):
    
    atm = None

    # Fixture that runs before every test
    @classmethod
    def setUpClass(self):
        self.atm = ATM(None)
        return 0

    def test_input_non_integer(self):
        self.assertEqual(self.atm.withdraw("blah"), -1)

    def test_input_negative(self):
        self.assertEqual(self.atm.withdraw(0), -1)
    
    def test_input_zero(self):    
        self.assertEqual(self.atm.withdraw(-1), -1)

    def test_10(self):
        self.assertEqual(self.atm.withdraw(10), "£20x0 £10x1")

    def test_20(self):
        self.assertEqual(self.atm.withdraw(20), "£20x1 £10x0")

    def test_30(self):
        self.assertEqual(self.atm.withdraw(30), "£20x1 £10x1")

    def test_40(self):
        self.assertEqual(self.atm.withdraw(40), "£20x2 £10x0")

    def test_50(self):
        self.assertEqual(self.atm.withdraw(50), "£20x2 £10x1")

if __name__ == '__main__':
    unittest.main()