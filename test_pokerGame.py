import unittest
from PokerGame import PokerGame_1


class TestPokerGame(unittest.TestCase):
    """测试创建扑克牌成功"""
    def test_create_instance(self):
        self.poker_game = PokerGame_1.PokerGame("2D 3D AD 4D 5D")
        self.assertTrue(isinstance(self.poker_game, PokerGame_1.PokerGame))


if __name__ == '__main__':
    unittest.main()

