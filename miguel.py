import unittest

def namecheck(x):
    return x == "MIGUEL"

class myTest(unittest.TestCase):

    def test(self):

        self.assertTrue(namecheck("CRUZ"))

if __name__ == '__main__':

    unittest.main()


