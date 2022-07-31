import unittest

import pytest


class Test_all(unittest.TestCase):

    def test_first(self):
        x = 4
        y = 5
        z = x + y
        print("addition is 9")
        print(z)
