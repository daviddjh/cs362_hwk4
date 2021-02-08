import unittest
import q1

class TestCalc(unittest.TestCase):
    def testVolume(self):
        self.assertEqual(q1.computeVolume(2),8,"should be equal to 8")              #int
        self.assertEqual(q1.computeVolume(3.5),42.875,"should be equal to 42.875")  #float
        with self.assertRaises(TypeError): q1.computeVolume("hello")                #string

if __name__ == "__main__":
    unittest.main()

