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
	
	def test_smaller(self):
		#Given
		s = 'abc'
		width=2#len(s)-1
		expected = s
		#when
		returned = string.center(s, width)
		#Then
		self.assertEqual(expected, returned)
		self.assertLess(width,len(s))

	def test_empty(self):
	    #Given
	    s = ''
	    width=2
	    expected = width*' '
	    #when
	    returned = string.center(s, width)
	    #Then
	    self.assertEqual(expected, returned)
	    
	def test_spaces(self):
	    #Given
	    s = ' abc '
	    width=7
	    expected = '  abc  '
	    #when
	    returned = string.center(s, width)
	    #Then
	    self.assertEqual(expected, returned)
	    
	def test_TypeError(self):
		#Given
		s = 'abc'
		width = 7
		list_fillchar = ['', 'ab']
		
		for fillch in list_fillchar:
			#Then
			with  self.assertRaises(TypeError):
				#When
				string.center(s, width, fillch)
		

if __name__ == '__main__': 
	unittest.main()
