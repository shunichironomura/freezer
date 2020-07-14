import unittest

import numpy as np
from functools import lru_cache
from unittest.mock import Mock

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

    def test_freezeargs_set(self):
        @of.freezeargs
        def func(s):
            return of.ishashable(s)

        s = {1, 2}
        self.assertFalse(of.ishashable(s))
        self.assertTrue(func(s))

    def test_freezeargs_dict_with_unhashable(self):
        @of.freezeargs
        def func(d):
            return of.ishashable(d)

        d = {1: [2, 3]}
        self.assertTrue(func(d))

    def test_freezeargs_with_lru_cache(self):
        mock = Mock() # for call counting

        @of.freezeargs
        @lru_cache(maxsize=None)
        def func(d, s):
            mock()
            return of.ishashable(d) and of.ishashable(s)

        d = {1: [2, 3]}
        s = {1, 2}
        self.assertEqual(mock.call_count, 0)
        func(d, s)
        self.assertEqual(mock.call_count, 1)
        func(d, s)
        # Does not increment since the result is in cache.
        self.assertEqual(mock.call_count, 1)




if __name__ == '__main__':
    unittest.main()