import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        b = False

        self.assertTrue(a, "a is not True")
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a = 'Test'
        b = 'test'

        self.assertEqual(a,b,"a is not equal to b")


if __name__=='__main__':
    unittest.main(verbosity=2)