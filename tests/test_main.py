import unittest
from src.main import main, get_emls

class TestMain(unittest.TestCase):
	def test_main(self):
		# Capture the output of the main function
		from io import StringIO
		import sys

		captured_output = StringIO()
		sys.stdout = captured_output
		main()
		sys.stdout = sys.__stdout__

		self.assertEqual(captured_output.getvalue().strip(), "Extracting IP addresses from emails...")

	def test_get_emls(self):
		# Test the get_emls function
		expected_emails = ["email1@example.com", "email2@example.com"]
		self.assertEqual(get_emls(), expected_emails)

if __name__ == "__main__":
	unittest.main()