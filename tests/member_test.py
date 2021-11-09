import unittest
from models.member import *

class TestCalculator(unittest.TestCase):

    def test_active_member_is_true(self):
        result = active_membership(True)
        self.assertEqual(True, result)