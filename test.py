def format_name(name):
    return name.capitalize()  # This will return 'Indar' for input 'indar'

# Example of a test
import unittest

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        upper_name = format_name("indar")
        self.assertEqual(upper_name, "Indar")  # This will now pass
