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

    def test_all_notes_available(self):
        self.assertEqual(self.atm.withdraw(100), "£50x2 £20x0 £10x0")
        self.assertEqual(self.atm.withdraw(90), "£50x1 £20x2 £10x0")
        self.assertEqual(self.atm.withdraw(80), "£50x1 £20x1 £10x1")
        self.assertEqual(self.atm.withdraw(70), "£50x1 £20x1 £10x0")
        self.assertEqual(self.atm.withdraw(60), "£50x1 £20x0 £10x1")
        self.assertEqual(self.atm.withdraw(50), "£50x1 £20x0 £10x0")
        self.assertEqual(self.atm.withdraw(40), "£50x0 £20x2 £10x0")
        self.assertEqual(self.atm.withdraw(30), "£50x0 £20x1 £10x1")
        self.assertEqual(self.atm.withdraw(20), "£50x0 £20x1 £10x0")
        self.assertEqual(self.atm.withdraw(10), "£50x0 £20x0 £10x1")

if __name__ == '__main__':
    unittest.main()