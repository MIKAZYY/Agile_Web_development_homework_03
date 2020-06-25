import unittest
from PokerGame import PokerGame_1


class TestGetScore(unittest.TestCase):
    def test_get_score_6(self):
        """测试得6分"""
        self.get_score = PokerGame_1.GetScore('2D 6D 7D 9D 5D')
        self.assertEqual(self.get_score.get_score(), 6)

    def test_get_score_7(self):
        """测试得7分"""
        self.get_score = PokerGame_1.GetScore('2D 3D AD 5D 4D')
        self.assertEqual(self.get_score.get_score(), 7)

    def test_get_score_5(self):
        """测试得5分"""
        self.get_score = PokerGame_1.GetScore('2D 4D 5D AD 3S')
        self.assertEqual(self.get_score.get_score(), 5)

    def test_get_score_4(self):
        """测试得4分"""
        self.get_score = PokerGame_1.GetScore('2D 2H 2S 3D 3S')
        self.assertEqual(self.get_score.get_score(), 4)

    def test_get_score_3(self):
        """测试得3分"""
        self.get_score = PokerGame_1.GetScore('2D 2C 2H 2S 3S')
        self.assertEqual(self.get_score.get_score(), 3)

    def test_get_score_2(self):
        """测试得2分"""
        self.get_score = PokerGame_1.GetScore('2D 2C 4H 7S 3S')
        self.assertEqual(self.get_score.get_score(), 2)

    def test_get_score_1(self):
        """测试得1分"""
        self.get_score = PokerGame_1.GetScore('2D 7C 4H AS 3S')
        self.assertEqual(self.get_score.get_score(), 1)


if __name__ == '__main__':
    unittest.main()