import unittest

class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#*" *30)
        print("Class 1 -> class set up method")
        print("#*" * 30)

    def setUp(self):
        print ("class 1 set up")

    def test_methodA(self):
        print ("class 1 method A")

    def test_methodB(self):
        print ("class 1 method B")

    def tearDown(self):
        print ("class 1 tear down")

    @classmethod
    def tearDownClass(cls):
        print("#*" *30)
        print("Class 1 -> class tear down method")
        print("#*" * 30)

if __name__=='__main__':
    unittest.main(verbosity=2)