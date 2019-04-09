import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """checks for Value Error when list is None"""
        tlist1 = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist1)

        """checks to return None when list is empty"""
        tlist2 = []
        self.assertEqual(max_list_iter(tlist2), None)

        """finds the maximum value in given list"""
        tlist3 = [-2,3,4,57,100293,32,-343084]
        self.assertEqual(max_list_iter(tlist3), 100293)
    
    def test_reverse_rec(self):
        """checks to determine if given list is reversed"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

        """checks longer list with negatives to determine if given list is reversed"""
        self.assertEqual(reverse_rec([-2,4,52,-1,5,7,9,-2,10]),[10,-2,9,7,5,-1,52,4,-2])

        """checks for ValueError if list is None"""
        tlist1 = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist1)

        """checks to see if [] are returned if list = []"""
        tlist2 = []
        self.assertEqual(tlist2, [])

    def test_bin_search(self):
        """finds the index of the target value, 4, given the parameters"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

        """checks for ValueError if list is None"""
        list_val2 = None
        low2 = -2
        high2 = len(list_val)-1
        with self.assertRaises(ValueError):
            bin_search(3, low2, high2, list_val2)

        """finds the index of the target value, -2, given the parameters"""
        list_val3 = [-9,-8,-7,-6,-5,-4,-3,-2,-1]
        low3 = 0
        high3 = len(list_val)-1
        self.assertEqual(bin_search(-2, low3, high3, list_val3), 7)

        """finds the index of the target value, -8, given the parameters"""
        list_val4 = [-9,-8,-7,-6,-5,-4,-3,-2,-1]
        low4 = 0
        high4 = 4
        self.assertEqual(bin_search(-8, low4, high4, list_val4), 1)
        
if __name__ == "__main__":
        unittest.main()

    
