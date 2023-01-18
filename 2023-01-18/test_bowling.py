import unittest
from bowlingscore import bowling_score

class TestBowlingScore(unittest.TestCase):
    def test_strike_game(self):
        rolls = "X X X X X X X X X X"
        expected_score = 300
        self.assertEqual(bowling_score(rolls), expected_score)

if __name__ == "__main__":
    unittest.main()