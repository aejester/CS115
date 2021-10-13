import unittest
import hw3

class Test(unittest.TestCase):

    def testGiveChange(self):
        self.assertEqual(hw3.giveChange(48, [1, 5, 10, 25, 50]), [6, [25, 10, 10, 1, 1, 1]])
        self.assertEqual(hw3.giveChange(48, [1, 7, 24, 42]), [2, [24, 24]])
        self.assertEqual(hw3.giveChange(35, [1, 3, 16, 30, 50]), [3, [16, 16, 3]])
    
    def testTake(self):
        self.assertEqual(hw3.take(3, [0, 1, 2, 3, 4, 5]), [0, 1, 2])
        self.assertEqual(hw3.take(1, [0, 1, 2, 3, 4, 5]), [0])
        self.assertEqual(hw3.take(0, [0, 1, 2, 3, 4, 5]), [])

    def testDrop(self):
        self.assertEqual(hw3.drop(1, [0, 1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(hw3.drop(2, [0, 1, 2, 3, 4, 5, 6]), [2, 3, 4, 5, 6])
        self.assertEqual(hw3.drop(0, [0, 1, 2, 3, 4, 5, 6]), [0, 1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()