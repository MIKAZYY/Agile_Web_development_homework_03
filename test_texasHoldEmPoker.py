import unittest
from PokerGame import PokerGame_1


class TestTexasHoldEmPoker(unittest.TestCase):
    def test_result_1(self):
        white = PokerGame_1.GetScore('2C 3H 4S 8C AH')
        black = PokerGame_1.GetScore('2H 3D 5S 9C KD')
        result = PokerGame_1.TexasHoldEmPoker.result(white, black)
        self.assertEqual(result, 'White wins')

    def test_result_2(self):
        white = PokerGame_1.GetScore('2S 8S AS QS 3S')
        black = PokerGame_1.GetScore('2H 4S 4C 2D 4H')
        result = PokerGame_1.TexasHoldEmPoker.result(white, black)
        self.assertEqual(result, 'White wins')

    def test_result_3(self):
        white = PokerGame_1.GetScore('2C 3H 4S 5C 6H')
        black = PokerGame_1.GetScore('2H 3H 5H 9H KH')
        result = PokerGame_1.TexasHoldEmPoker.result(white, black)
        self.assertEqual(result, 'Black wins')

    def test_result_4(self):
        white = PokerGame_1.GetScore('2D 3H 5C 9S KH')
        black = PokerGame_1.GetScore('2H 3D 5S 9C KD')
        result = PokerGame_1.TexasHoldEmPoker.result(white, black)
        self.assertEqual(result, 'Tie')

    def test_result_5(self):
        white = PokerGame_1.GetScore('2D 2H 5C 5S KH')
        black = PokerGame_1.GetScore('3H 3D 5H 5D KD')
        result = PokerGame_1.TexasHoldEmPoker.result(white, black)
        self.assertEqual(result, 'Black wins')


if __name__ == '__main__':
    unittest.main()