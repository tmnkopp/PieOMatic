import unittest 
from pyomatic.converters import Convert  

class MyTest(unittest.TestCase):
    def test(self):
        _convert = Convert()
        per = Convert().to_percent(2,4)
        print(per)
        self.assertEqual(per, 50.0)
        
        
if __name__ == '__main__':
    unittest.main()        