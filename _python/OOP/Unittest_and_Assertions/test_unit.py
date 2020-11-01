#import the python testing framework
import unittest

#our "unit"
# this is what we are running or test on
def reverseArray(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list

def anotherFunction(list):
    pass

# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase

class anotherFunctionTests(unittest.TestCase):
    # each method in this case is a test to be run
    def testOne(self):
        self.assertEqual(reverseArray([1,2,3]), [3,2,1])
    def testTwo(self):
        self.assertEqual(reverseArray([5,4,3,2,1]), [1,2,3,4,5])
    # any task you wnat run before any method above is executed, put them in the ..
    def setUp(self):
        print("running setUp")

    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # this runs our test