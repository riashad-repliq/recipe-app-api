from django.test import SimpleTestCase
from app import calc

class SumTest(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(6,6)
        
        self.assertEqual(res, 12)
    
    def test_sub_numbers(self):
        res = calc.sub(10, 1)
        
        self.assertEqual(res, 9)  
    