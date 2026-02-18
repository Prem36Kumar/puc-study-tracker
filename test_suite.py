import unittest
from analytics import calculate_grade


class TestAnalytics(unittest.TestCase):

    def test_calculate_grade(self):
        # A grade
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(90), "A")

        # B grade
        self.assertEqual(calculate_grade(80), "B")
        self.assertEqual(calculate_grade(75), "B")

        # C grade
        self.assertEqual(calculate_grade(70), "C")
        self.assertEqual(calculate_grade(60), "C")

        # D grade
        self.assertEqual(calculate_grade(55), "D")
        self.assertEqual(calculate_grade(50), "D")

        # F grade
        self.assertEqual(calculate_grade(40), "F")
        self.assertEqual(calculate_grade(0), "F")


if __name__ == "__main__":
    unittest.main()


