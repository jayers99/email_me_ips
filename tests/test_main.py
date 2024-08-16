import unittest
from src.main import main

class TestMain(unittest.TestCase):
	def test_main(self):
		# Capture the output of the main function
		from io import StringIO
		import sys

		captured_output = StringIO()
		sys.stdout = captured_output
		main()
		sys.stdout = sys.__stdout__

		self.assertEqual(captured_output.getvalue().strip(), "Hello, this is your CLI tool!")

if __name__ == "__main__":
	unittest.main()