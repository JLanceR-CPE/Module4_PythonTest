import unittest

def multiply(x,y):

    return x*y

class myTest(unittest.TestCase):

    def test(self):

        self.assertEqual(multiply(5,5),25)

if __name__ == '__main__':

    unittest.main()
