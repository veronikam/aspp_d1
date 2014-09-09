import unittest
from maxima import find_maxima

class TestLocalMaxima(unittest.TestCase):

    def test_last_index(self):
        #Given
        x = [4, 2, 1, 3, 1, 2]
        expected_ind = [0, 3, 5]
        #When
        returned_ind = find_maxima(x)
        #Then
        self.assertEqual(expected_ind, returned_ind)

if __name__=="__main__":
    unittest.main()
