import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('kala'.upper(),'KALA')

    def test_isupper(self):
        self.assertTrue('KALA'.isupper())
        self.assertFalse('Kala'.isupper())
    def test_split(self):
        s='hello world'
        self.assertEqual(s.split(),['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


    if __name__ =='__main__':
        unittest.main()
        
