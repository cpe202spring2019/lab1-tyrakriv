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

        """finds max value in positive list"""
        tlist4 = [1,2,3]
        self.assertEqual(max_list_iter(tlist4), 3)

        """finds max value in decimal and integers"""
        tlist5 = [5.4,4.8,3,3]
        self.assertAlmostEqual(max_list_iter(tlist5), 5.4)

        """finds max value in float list"""
        tlist6 = [4.8,5.4,3.3]
        self.assertAlmostEqual(max_list_iter(tlist6), 5.4)

        """finds max value of negative list"""
        tlist7 = [-3,-1,-6]
        self.assertAlmostEqual(max_list_iter(tlist7), -1)

        """finds max value of list with one item"""
        tlist8 = [9]
        self.assertAlmostEqual(max_list_iter(tlist8), 9)

    
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

        """checks float list"""
        self.assertEqual(reverse_rec([5.4,4.3,2.2]),[2.2,4.3,5.4])

        """checks a list with one value"""
        self.assertEqual(reverse_rec([-1]),[-1])

        """checks list with negatives"""
        self.assertEqual(reverse_rec([-3,-4,-5]),[-5,-4,-3])

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

        """checks if index is not found"""
        list_val5 = [-9,-8,-7,-6,-5,-4,-3,-2,-1]
        low5 = 0
        high5 = 4
        self.assertEqual(bin_search(5, low5, high5, list_val5), None)

        list_val6 =[0,1,2,3,4]
        low6 = 0
        high6 = len(list_val)-1
        """checks if index is in the middle"""
        self.assertEqual(bin_search(2, 0, len(list_val6)-1, list_val6), 2 )

        """checks an empty list"""
        self.assertEqual(bin_search(2, 0, len(list_val6)-1, []), None)
        
        """checks float list"""
        self.assertEqual(bin_search(0.3,0,3,[0.1,0.2,0.3,0.4]), 2)

        """checks if low and high is the same value"""
        self.assertEqual(bin_search(5,0,0,[5]),0)

        """checks when low and high do not contain the search value"""
        self.assertEqual(bin_search(2,3,4,[1,2,3,4,5]),None)

        """checks when low and high do not contain the search value"""
        self.assertEqual(bin_search(5,0,3,[1,2,3,4,5]),None)

        """checks if value is not in the list"""
        self.assertEqual(bin_search(3,0,4,[0,1,2,4,5]),None)
        
if __name__ == "__main__":
        unittest.main()

    
