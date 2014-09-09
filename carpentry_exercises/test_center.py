import unittest
import string


class FunctionalityTest(unittest.TestCase):

	def test_odd_even_widths(self):
		#Given
		s = 'abc'
		
		#When
		expected = ' abc '
		returned = string.center(s, 5)
				
		#Then
		self.assertEqual(returned, expected)

if __name__ == '__main__': 
	unittest.main()
