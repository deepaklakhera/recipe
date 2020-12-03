from django.test import TestCase
from .calc import add,sub

class CacTest(TestCase):

    def test_calc(self):
        self.assertEqual(add(2,3),5)

    def test_sub(self):
        self.assertEqual(sub(3,2),1)
        self.assertEqual(sub(-3,-2),-1)
        self.assertEqual(sub(-3,2),-1)
        self.assertEqual(sub(-3,-4),1)
        