import unittest
import math
import sphere

class sphereTest(unittest.TestCase):

    #these need to be updated for a sphere
    def test_volume1(self):
        assert(sphere.volume(10) == (4.0/3.0) * math.pi * 10**3)

    def test_volume2(self):
        assert(sphere.volume(100) == (4.0/3.0) * math.pi * 100**3)

    def test_volume3(self):
        assert(sphere.volume(0) == 0.0)

    #failing test
    #def test_volume3(self):
        #assert(sphere.volume(10,1000) == ??)


if __name__ == '__main__':
    unittest.main()
