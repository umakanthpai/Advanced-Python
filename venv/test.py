import unittest
import unitTesting


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("Setting up tests")

    def test_sqrt_1(self):
        '''
        Square root test
        :return:
        '''
        # This will be called for every test method
        ut = unitTesting.UnitTesting()
        result = ut.squareRoot(25)
        self.assertEqual(result, 5)

    def test_sqrt_2(self):
        '''
        TypeError exception test
        :return:
        '''
        ut = unitTesting.UnitTesting()
        self.assertRaises(TypeError,ut.squareRoot,"25")

    def tearDown(self):
        # This will be called for every test method
        print('Tearing down')

if __name__ == '__main__':
    unittest.main()
