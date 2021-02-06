import unittest
import cal

#To run this code: python3 test_cal.py 

class TestCal(unittest.TestCase):
	def test_cube(self):
   		# Standard input and expected output
		self.assertEqual(cal.cube_volume(2, 2, 2), 8)
	
		# Negative input should result in error being thrown (represented here with 0) but not fail
		self.assertEqual(cal.cube_volume(4, -2, 2), 0)

		# Incorrect type should result in an error being thrown (error represented as 0) but not fail
		self.assertEqual(cal.cube_volume("5", 2, 1), 0)

	def test_aver(self):
		# Standard input should return expected output
		self.assertEqual(cal.aver_list([2, 2, 2, 2]), 2)

		# Empty array should return an error (represented with 0) but not fail
		self.assertEqual(cal.aver_list([]), 0)
		
		# Arrays with negatives and floats should return expected output
		self.assertEqual(cal.aver_list([-3, 3.5, 4.2, 8]), 3.175)

	def test_make(self):
		# Standard input should result in expected output
		self.assertEqual(cal.make_name("John", "Doe"), "John Doe")

		# Empty string should result in an error being thrown and catched
		self.assertEqual(cal.make_name("", "Paige"), 0)
		
		# Neither input is of the correct type so an error should be thrown and catched
		self.assertEqual(cal.make_name(8.7, 8), 0)


if __name__ == "__main__":
	unittest.main()
