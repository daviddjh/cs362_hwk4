import unittest
import q3

class TestCalc(unittest.TestCase):
    def testAvg(self):
        self.assertEqual(q3.fullName("david", "headrick"),"david headrick","should be equal to \"david headrick\"")           #my name
        with self.assertRaises(TypeError): q3.fullName(39, 39)                              #ints
        with self.assertRaises(TypeError): q3.fullName("david", 40)                         #int and string

if __name__ == "__main__":
    unittest.main()