import unittest

import numpy as np

import object_freezer as of

class TestCore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # procedures before tests are started. This code block is executed only once
        pass

    @classmethod
    def tearDownClass(cls):
        # procedures after tests are finished. This code block is executed only once
        pass

    def setUp(self):
        # procedures before every tests are started. This code block is executed every time
        pass

    def tearDown(self):
        # procedures after every tests are finished. This code block is executed every time
        pass

    def test_ishashable(self):
        # Check hashable objects
        self.assertTrue(of.ishashable(1)) # int
        self.assertTrue(of.ishashable('a')) # str
        self.assertTrue(of.ishashable(1.2)) # float
        self.assertTrue(of.ishashable((1, 2))) # tuple

        # Check non-hashable objects
        self.assertFalse(of.ishashable([1, 2])) # list
        self.assertFalse(of.ishashable({1: 2})) # dict
        self.assertFalse(of.ishashable({1, 2})) # set
        self.assertFalse(of.ishashable((1, [1, 2]))) # tuple with a list element

    def test_freeze_simple_objects(self):
        self.assertTrue(of.ishashable(of.freeze([1, 2]))) # list
        self.assertTrue(of.ishashable(of.freeze({1: 2}))) # dict
        self.assertTrue(of.ishashable(of.freeze({1, 2}))) # set

    def test_freeze_tuple_with_unhashable(self):
        t = (1, [1, 2])
        self.assertFalse(of.ishashable(t))
        ft = of.freeze(t)
        self.assertTrue(of.ishashable(ft))
        self.assertEqual(t[1][0], ft[1][0])

    def test_freeze_dict_with_unhashable(self):
        d = {'a': ['b', 2]}
        fd = of.freeze(d)
        self.assertTrue(of.ishashable(fd))
        self.assertEqual(fd['a'][0], d['a'][0])

    def test_freeze_numpy_array_with_custom_conversion(self):
        a = np.arange(4)
        self.assertFalse(of.ishashable(a))

        cc = {np.ndarray: lambda a: tuple(a)}

        fa = of.freeze(a, custom_conversions=cc)
        self.assertTrue(of.ishashable(fa))
        self.assertIsInstance(fa, tuple)
        self.assertEqual(fa[0], a[0])

    def test_freeze_dict_with_numpy_array(self):
        a = np.arange(4)
        d = {'a': a}
        cc = {np.ndarray: tuple}

        fd = of.freeze(d, custom_conversions=cc)
        self.assertTrue(of.ishashable(fd))
        self.assertIsInstance(fd, of.deepfrozendict)
        self.assertIsInstance(fd['a'], tuple)
        self.assertEqual(fd['a'][0], d['a'][0])

if __name__ == '__main__':
    unittest.main()