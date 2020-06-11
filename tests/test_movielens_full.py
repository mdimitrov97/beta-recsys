import os
import sys
import unittest

sys.path.append("../")

from beta_rec.datasets.movielens import Movielens_100k


class TestMovielens(unittest.TestCase):
    def test_preprocess(self):
        ml_100k = Movielens_100k()
        ml_100k.preprocess()
        self.assertTrue(os.path.exists(os.getcwd() + "/datasets/ml_100k/raw/ml_100k"))
        self.assertTrue(os.path.exists(os.getcwd() + "/datasets/ml_100k/raw/ml_100k"))
        self.assertTrue(
            os.path.exists(
                os.getcwd() + "/datasets/ml_100k/processed/ml_100k_interaction.npz"
            )
        )

        interactions = ml_100k.load_interaction()
        self.assertEqual(100000, interactions.shape[0])
        self.assertEqual(4, interactions.shape[1])