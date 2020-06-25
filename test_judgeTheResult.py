import unittest
from PokerGame import PokerGame_1


class TestGetScore(unittest.TestCase):

    def test_is_flush(self):
        """判断是同花"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 6D 7D 9D 5D")
        self.assertTrue(self.get_score.is_flush())

    def test_is_flush_2(self):
        """判断是同花"""
        self.get_score = PokerGame_1.JudgeTheResult("2D AD 7D 9D JD")
        self.assertTrue(self.get_score.is_flush())

    def test_is_flush_3(self):
        """判断不是同花"""
        self.get_score = PokerGame_1.JudgeTheResult("2D AS 7D 9D JD")
        self.assertFalse(self.get_score.is_flush())

    def test_is_straight(self):
        """判断不是顺子"""
        self.get_score = PokerGame_1.JudgeTheResult("4S 3D AD 4D 5D")
        self.assertFalse(self.get_score.is_straight())

    def test_is_straight_2(self):
        """判断是顺子"""
        self.get_score = PokerGame_1.JudgeTheResult("TD QD JD AD KD")
        self.assertTrue(self.get_score.is_straight())

    def test_is_straight_3(self):
        """判断是顺子"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 4D 5D AD 3D")
        self.assertTrue(self.get_score.is_straight())

    def test_is_straight_flush(self):
        """判断不是同花顺"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 3D AD 5D 4S")
        self.assertFalse(self.get_score.is_straight_flush())

    def test_is_straight_flush_2(self):
        """判断是同花顺"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 3D AD 5D 4D")
        self.assertTrue(self.get_score.is_straight_flush())

    def test_is_straight_flush_3(self):
        """判断是同花顺"""
        self.get_score = PokerGame_1.JudgeTheResult("8D JD 9D QD TD")
        self.assertTrue(self.get_score.is_straight_flush())

    def test_is_three_of_a_kind(self):
        """判断不是三张"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 3D AD 5D 4S")
        self.assertFalse(isinstance(self.get_score.is_three_of_a_kind(), str))

    def test_is_three_of_a_kind_2(self):
        """判断不是三张"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2H 5D 3D 3S")
        self.assertFalse(isinstance(self.get_score.is_three_of_a_kind(), str))

    def test_is_three_of_a_kind_3(self):
        """判断不是三张"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2H 2S 2C 3S")
        self.assertFalse(isinstance(self.get_score.is_three_of_a_kind(), str))

    def test_is_three_of_a_kind_4(self):
        """判断是三张"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2H 2S 3D 3S")
        self.assertTrue(isinstance(self.get_score.is_three_of_a_kind(), str))

    def test_is_two_pairs(self):
        """判断是两对"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2C 6D 3D 3S")
        self.assertTrue(isinstance(self.get_score.is_two_pairs(), list))

    def test_is_two_pairs_2(self):
        """判断是两对"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2C 2H 2S 3S")
        self.assertTrue(isinstance(self.get_score.is_two_pairs(), list))

    def test_is_one_pairs(self):
        """判断不是一对"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2C 2H 3S 3S")
        self.assertFalse(isinstance(self.get_score.is_one_pairs(), str))

    def test_is_one_pairs_2(self):
        """判断不是一对"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2C 4H 3S 3S")
        self.assertFalse(isinstance(self.get_score.is_one_pairs(), str))

    def test_is_one_pairs_3(self):
        """判断不是一对"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2C 2H 2S 3S")
        self.assertFalse(isinstance(self.get_score.is_one_pairs(), str))

    def test_is_one_pairs_4(self):
        """判断是一对"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 8C 8H 5S 3S")
        self.assertTrue(isinstance(self.get_score.is_one_pairs(), str))

    def test_is_high_card(self):
        """判断是散牌"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 7C 4H AS 3S")
        self.assertTrue(self.get_score.is_high_card())

    def test_is_high_card_2(self):
        """判断不是散牌"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 3D 4D 5D AD")
        self.assertFalse(self.get_score.is_high_card())

    def test_is_high_card_3(self):
        """判断不是散牌"""
        self.get_score = PokerGame_1.JudgeTheResult("2S 3D 4D 5D AD")
        self.assertFalse(self.get_score.is_high_card())

    def test_is_high_card_4(self):
        """判断不是散牌"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 3D JD 5D AD")
        self.assertFalse(self.get_score.is_high_card())

    def test_is_high_card_5(self):
        """判断不是散牌"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2S 2C 3D 4D")
        self.assertFalse(self.get_score.is_high_card())

    def test_is_high_card_6(self):
        """判断不是散牌"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2S 2C 2D 4D")
        self.assertFalse(self.get_score.is_high_card())

    def test_is_high_card_7(self):
        """判断不是散牌"""
        self.get_score = PokerGame_1.JudgeTheResult("2D 2S 6C 9D 4D")
        self.assertFalse(self.get_score.is_high_card())


if __name__ == '__main__':
    unittest.main()


