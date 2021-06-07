import unittest
import question1

class TestCase(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(question1.reverseString("This is four words"), "words four is This")
        self.assertEqual(question1.reverseString("Work with ##number1234"), "##number1234 with Work")

#enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)