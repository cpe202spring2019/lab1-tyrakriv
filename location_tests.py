import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        """Tests the location of SLO to find if it represented correctly"""
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1),"Location(SLO,35.3,-120.7)")

        """Tests the location of Tokyo to find if it represented correctly"""
        loc2 = Location("Tokyo", 178.2, -5.4)
        self.assertEqual(repr(loc2),"Location(Tokyo,178.2,-5.4)")

        """Tests the location of Seattle to find if it represented correctly"""
        loc3 = Location("Seattle", 70.8, 117.3)
        self.assertEqual(repr(loc3),"Location(Seattle,70.8,117.3)")
        
    def test_eq(self):
        """Tests the eq function to determine if a location matches its description"""
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc1 == Location("SLO", 35.3, -120.7))
        
        """Tests if the locations of Tokyo and Seattle are the same"""
        loc2 = Location("Tokyo", 178.2, -5.4)
        loc3 = Location("Seattle", 70.8, -117.3)
        self.assertFalse(loc2 == loc3)

    def test_init(self):
        """Checks init function to determine if the objects in the class are correct"""
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1.name, 'SLO')
        self.assertEqual(loc1.lat, 35.3)
        self.assertEqual(loc1.lon, -120.7)

        """Checks init function to determine if the objects in the class are correct"""
        loc2 = Location("Tokyo", 178.2, -5.4)
        self.assertEqual(loc2.name, 'Tokyo')
        self.assertEqual(loc2.lat, 178.2)
        self.assertEqual(loc2.lon, -5.4)

if __name__ == "__main__":
        unittest.main()
