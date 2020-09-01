import unittest
import pickle
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

    def test_pickle(self):
        obj = (
            of.deepfrozendict({1: 2}),
            of.deepfrozendict({2: 3})
        )
        obj_hash = hash(obj)

        pkl_path = 'obj.pkl'

        pickle_bytes = pickle.dumps(obj)

        loaded_obj = pickle.loads(pickle_bytes)
        loaded_obj_hash = hash(loaded_obj)

        self.assertEqual(obj_hash, loaded_obj_hash)

        new_obj = (
            of.deepfrozendict({1: 2}),
            of.deepfrozendict({2: 3})
        )
        new_obj_hash = hash(new_obj)
        self.assertEqual(loaded_obj_hash, new_obj_hash)


if __name__ == '__main__':
    unittest.main()