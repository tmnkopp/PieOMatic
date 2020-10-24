import unittest 
from pyomatic.converters import Convert  

class MyTest(unittest.TestCase):
    def test_to_percent(self): 
        per = Convert().to_percent(2,4) 
        self.assertEqual(per, 50.0)

    def test_to_percentf(self): 
        per = Convert().to_percentf(2,4)  
        self.assertEqual(per, '50%')        
        
if __name__ == '__main__':
    unittest.main()        