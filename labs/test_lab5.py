import unittest
from lab5 import fastED

class Test(unittest.TestCase):

    def testFastED(self):
        self.assertEqual(fastED("antidisestablishment", "antiquities"), 13)
        self.assertEqual(fastED("xylophone", "yellow"), 7)
        self.assertEqual(fastED("follow", "yellow"), 2)
        self.assertEqual(fastED("lower", "hover"), 2)

if __name__ == "__main__":
    unittest.main()