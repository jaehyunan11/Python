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


if __name__ == '__main__':
    unittest.main() # this runs our test