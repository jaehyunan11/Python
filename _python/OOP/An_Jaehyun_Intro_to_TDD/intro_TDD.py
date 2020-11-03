import unittest
from function_list import *

class FunctionalTest(unittest.TestCase):

    def setUP(self):
        print("setUp")
        pass

    def tearDown(self):
        print("teardown")
        pass

    def test_reverse_list(self):
        print("test_reverse_list")
        self.assertEqual(reverseList([1,3,5,7,9]), [9,7,5,3,1])
        self.assertEqual(reverseList([1,3,5,7]), [7,5,3,1])
        self.assertEqual(reverseList([1,3,5,7,9,12]), [12,9,7,5,3,1])

    def test_palidrome_list(self):
        print("test_palidrome_list")
        self.assertEqual(isPalidrome("malayalam"), True)
        self.assertEqual(isPalidrome("malayalamf"), False)
        self.assertEqual(isPalidrome("anna"), True)
        self.assertEqual(isPalidrome("civic"), True)
        self.assertEqual(isPalidrome("racecars"), False)

    def test_coins_list(self):
        print("test_coins_list")
        self.assertEqual(coins(50), {'quarter': 2})
        self.assertEqual(coins(124),{'quarter': 4, 'dime': 2, 'nickel': 0, 'penny': 4})
        self.assertEqual(coins(1113), {'quarter': 44, 'dime': 1, 'nickel': 0, 'penny': 3})
        self.assertEqual(coins(11134), {'quarter': 445, 'dime': 0, 'nickel': 1, 'penny': 4})
        self.assertEqual(coins(135244), {'quarter': 5409, 'dime': 1, 'nickel': 1, 'penny': 4})


if __name__ == '__main__':
    unittest.main() # this runs our test