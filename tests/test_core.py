import unittest

import numpy as np

from freezer.core import *

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
        self.assertTrue(ishashable(1)) # int
        self.assertTrue(ishashable('a')) # str
        self.assertTrue(ishashable(1.2)) # float
        self.assertTrue(ishashable((1, 2))) # tuple

        # Check non-hashable objects
        self.assertFalse(ishashable([1, 2])) # list
        self.assertFalse(ishashable({1: 2})) # dict
        self.assertFalse(ishashable({1, 2})) # set
        self.assertFalse(ishashable((1, [1, 2]))) # tuple with a list element

    def test_freeze_simple_objects(self):
        self.assertTrue(ishashable(freeze([1, 2]))) # list
        self.assertTrue(ishashable(freeze({1: 2}))) # dict
        self.assertTrue(ishashable(freeze({1, 2}))) # set

    def test_freeze_tuple_with_unhashable(self):
        t = (1, [1, 2])
        self.assertFalse(ishashable(t))
        ft = freeze(t)
        self.assertTrue(ishashable(ft))
        self.assertEqual(t[1][0], ft[1][0])

    def test_freeze_dict_with_unhashable(self):
        d = {'a': ['b', 2]}
        fd = freeze(d)
        self.assertTrue(ishashable(fd))
        self.assertEqual(fd['a'][0], d['a'][0])

    def test_freeze_numpy_array_with_custom_conversion(self):
        a = np.arange(4)
        self.assertFalse(ishashable(a))

        cc = {np.ndarray: lambda a: tuple(a)}

        fa = freeze(a, custom_conversions=cc)
        self.assertTrue(ishashable(fa))
        self.assertIsInstance(fa, tuple)
        self.assertEqual(fa[0], a[0])

    def test_freeze_dict_with_numpy_array(self):
        a = np.arange(4)
        d = {'a': a}
        cc = {np.ndarray: tuple}

        fd = freeze(d, custom_conversions=cc)
        self.assertTrue(ishashable(fd))
        self.assertIsInstance(fd, deepfrozendict)
        self.assertIsInstance(fd['a'], tuple)
        self.assertEqual(fd['a'][0], d['a'][0])

if __name__ == '__main__':
    unittest.main()