import unittest
import string


class FunctionalityTest(unittest.TestCase):

	def test_odd_even_widths(self):
		#Given
		s = 'abc'
		assert_list = [(5, ' abc ', ' abc '), (4, 'abc ', ' abc')]
		
		for row in assert_list:
		    #When
		    returned = string.center(s, row[0])
			#Then
		    self.assertTrue(returned==row[1] or returned==row[2])

if __name__ == '__main__': 
	unittest.main()
