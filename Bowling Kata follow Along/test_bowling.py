import unittest


def compute_score(frames_scores):
    score = 0
    rolls = 0
    for index, frame_score in enumerate(frames_scores):
        if rolls >= 20:
            break
        if frame_score == '/':
            score += spare_score(frames_scores, index)
        elif frame_score == 'X':
            rolls += 1
            score += strike_score(frames_scores, index)
        elif frame_score != '-':
            score += int(frame_score)
        rolls += 1
    return score

def spare_score(frames_scores, index):
    return 10 - frame_value(frames_scores[index-1]) + frame_value(frames_scores[index + 1])

def strike_score(frame_scores, index):
    if frame_scores[index+2] == '/':
        return 20
    return 10 + frame_value(frame_scores[index + 1]) + frame_value(frame_scores[index + 2])

def frame_value(frame):
    if frame == "X":
        return 10
    if frame == "/":
        return 10
    if frame == "-":
        return 0
    return int(frame)


class BowlingTest(unittest.TestCase):
    def test_all_zeros(self):
        frames = "--------------------"
        score = compute_score(frames)
        self.assertEqual(score, 0)

    def test_all_ones(self):
        frames = "11111111111111111111"
        score = compute_score(frames)
        self.assertEqual(score, 20)

    def test_a_spare(self):
        frames = "1/111111111111111111"
        score = compute_score(frames)
        self.assertEqual(score, 29)

    def test_a_strike(self):
        frames = "X111111111111111111"
        score = compute_score(frames)
        self.assertEqual(score, 30)

    def test_a_spare_then_strike(self):
        frames = "1/X1111111111111111"
        score = compute_score(frames)
        self.assertEqual(score, 48)
    
    def test_three_strikes(self):
        frames = "XXX11111111111111"
        score = compute_score(frames)
        self.assertEqual(score, 30+21+12+14)

    def test_a_spare_with_zero(self):
        frames = "1/-11111111111111111"
        score = compute_score(frames)
        self.assertEqual(score, 27)

    def test_perfect_game(self):
        frames = "XXXXXXXXXXXX"
        score = compute_score(frames)
        self.assertEqual(score, 300)

    def test_spare_at_end(self):
        frames = "-------------------/5"
        score = compute_score(frames)
        self.assertEqual(score, 15)
    
    def test_almost_perfect_game(self):
        frames = "XXXXXXXXXX9/"
        score = compute_score(frames)
        self.assertEqual(score, 289)


if __name__ == "__main__":
    unittest.main()