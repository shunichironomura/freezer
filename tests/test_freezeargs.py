import unittest

import numpy as np
from functools import lru_cache
from unittest.mock import Mock

from freezer.core import *
from freezer.freezeargs import freezeargs


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
        @freezeargs
        def func(s):
            return ishashable(s)

        s = {1, 2}
        self.assertFalse(ishashable(s))
        self.assertTrue(func(s))

    def test_freezeargs_dict_with_unhashable(self):
        @freezeargs
        def func(d):
            return ishashable(d)

        d = {1: [2, 3]}
        self.assertTrue(func(d))

    def test_freezeargs_with_lru_cache(self):
        mock = Mock() # for call counting

        @freezeargs
        @lru_cache(maxsize=None)
        def func(d, s):
            mock()
            return ishashable(d) and ishashable(s)

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