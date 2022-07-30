import unittest

import pytest

class Testtall(unittest.TestCase):


    def test_first(self):
        x = 4
        y = 5
        z = x + y
        print("addition is 9")
        print(z)