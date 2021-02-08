import unittest
import q2

class TestCalc(unittest.TestCase):
    def testAvg(self):
        self.assertEqual(q2.calcAvgValue([1,2,3,4]),2.5,"should be equal to 2.5")           #int
        self.assertEqual(q2.calcAvgValue([1.5,2.5,3.5,4.5]),3,"should be equal to 3")       #int
        with self.assertRaises(TypeError): q2.calcAvgValue("hello")                         #string
        with self.assertRaises(ValueError): q2.calcAvgValue(["he", "helo", 3, 3.5])         #string in list
        with self.assertRaises(ValueError): q2.calcAvgValue([])                             #empty list

if __name__ == "__main__":
    unittest.main()