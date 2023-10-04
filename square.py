import unittest

def area(l,w):
    
    return l*w

def perimeter(a,b,c,d):
    
    return a*b*c*d
   
class myTest(unittest.TestCase):

    def test(self):

        self.assertTrue(area(2,2),4)
    
    def test(self):
        self.assertEqual(perimeter(2,2,2,2),16)

if __name__ == '__main__':

    unittest.main()