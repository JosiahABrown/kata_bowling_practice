import unittest

def calc_score(frames_scores):
    score, rolls = 0, 0
    for index, frame in enumerate(frames_scores):
        if rolls >= 20:
            break
        if frame == 'X':
            rolls += 1
            score += strike_score(frames_scores, index)
        elif frame == '/':
            score += spare_score(frames_scores, index)
        elif frame != '-':
            score += int(frame)
        rolls += 1
    return score

def frame_value(frame):
    if frame == 'X':
        return 10
    if frame == '/':
        return 10
    if frame == '-':
        return 0
    return int(frame)

def spare_score(frame_scores, index):
    return 10 - frame_value(frame_scores[index-1]) + frame_value(frame_scores[index+1])

def strike_score(frame_scores, index):
    if frame_scores[index+2] == '/':
        return 20
    return 10 + frame_value(frame_scores[index+1]) + frame_value(frame_scores[index+2])

class TestBowlingScore(unittest.TestCase):
    def test_all_zeros(self):
        frames = '--------------------'
        score = calc_score(frames)
        self.assertEqual(score, 0)
    
    def test_all_ones(self):
        frames = '11111111111111111111'
        score = calc_score(frames)
        self.assertEqual(score, 20)
    
    def test_one_spare(self):
        frames = '1/111111111111111111'
        score = calc_score(frames)
        self.assertEqual(score, 29)
        
    def test_one_strike(self):
        frames = 'X111111111111111111'
        score = calc_score(frames)
        self.assertEqual(score, 30)

    def test_miss_regular_game(self):
        frames = '9-9-9-9-9-9-9-9-9-9-'
        score = calc_score(frames)
        self.assertEqual(score, 90)
    
    def test_almost_perfect_game(self):
        frames = 'XXXXXXXXXX9/'
        score = calc_score(frames)
        self.assertEqual(score, 289)
    
    def test_perfect_game(self):
        frames = 'XXXXXXXXXXXX'
        score = calc_score(frames)
        self.assertEqual(score, 300)

if __name__ == '__main__':
    unittest.main()
