class PokerGame:

    def __init__(self, string_of_cards):
        self.cards = string_of_cards.split()
        rule = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
        dic = {'T': chr(58), 'J': chr(59), 'Q': chr(60), 'K': chr(61), 'A': chr(62)}
        self.cards.sort(key=lambda m: rule[m[0]])
        self.cards = [dic[i[0]] + i[1] if i[0] in dic else i for i in self.cards]


class JudgeTheResult(PokerGame):
    """判断手牌结果"""

    def is_flush(self):
        """判断是否为同花"""
        first_suite = self.cards[0][1]
        for card in self.cards[1:]:
            if first_suite != card[1]:
                return False
        return True

    def is_straight(self):
        """判断是否是顺子"""
        temp_card_num = self.cards[0][0]
        flag = True
        for temp_card in self.cards[1:]:
            if ord(temp_card[0]) == ord(temp_card_num)+1:
                temp_card_num = temp_card[0]
                flag = True
            else:
                flag = False
                break
        if not flag and self.cards[4][0] == chr(62):
            temp_card_num = '1'
            for temp_card in self.cards[:4]:
                if ord(temp_card[0]) == ord(temp_card_num) + 1:
                    temp_card_num = temp_card[0]
                    flag = True
                else:
                    flag = False
                    break
        return flag

    def is_straight_flush(self):
        """判断是否为同花顺"""
        if self.is_flush() and self.is_straight():
            return True
        return False

    def is_three_of_a_kind(self):
        """判断是否为三张"""
        signal_card_num = self.cards[0][0]
        count = 1
        is_three = False
        is_four = False
        card_to_be_cmp = signal_card_num
        for card in self.cards[1:]:
            if card[0] == signal_card_num:
                count += 1
                if count == 3:
                    card_to_be_cmp = signal_card_num
                    is_three = True
                if count == 4:
                    is_four = True
            else:
                signal_card_num = card[0]
                count = 1
        if is_three and not is_four:
            return card_to_be_cmp
        return False

    def is_two_pairs(self):
        """判断是否为两对"""
        if self.is_three_of_a_kind():
            return False
        first_pair_num = self.cards[0][0]
        flag = [0, 0]
        count = 1
        card_to_be_cmp = []
        for card in self.cards[1:]:
            count += 1
            if card[0] == first_pair_num:
                flag[0] = 1
                card_to_be_cmp.append(first_pair_num)
                break
        if flag[0] == 1:
            second_pair_num = self.cards[count][0]
            for card in self.cards[count+1:]:
                if card[0] == second_pair_num:
                    flag[1] = 1
                    card_to_be_cmp.append(second_pair_num)
                    break
        if flag == [1, 1]:
            return card_to_be_cmp
        return False

    def is_one_pairs(self):
        """判断是否为对子"""
        if self.is_three_of_a_kind() or self.is_two_pairs():
            return False
        signal_pair_num = self.cards[0][0]
        flag = 0
        card_to_be_cmp = signal_pair_num
        for card in self.cards[1:]:
            if card[0] == signal_pair_num:
                flag = 1
                card_to_be_cmp = signal_pair_num
                break
            else:
                signal_pair_num = card[0]
        if flag:
            return card_to_be_cmp
        return False

    def is_high_card(self):
        """判断是否为散牌"""
        if not self.is_two_pairs() and not self.is_one_pairs() and not self.is_flush() \
                and not self.is_straight() and not self.is_three_of_a_kind():
            return True
        return False


class GetScore(JudgeTheResult):

    def get_score(self):
        """若是同花顺，得7分；
           若是同花，得6分；
           若是顺子，得5分；
           若是三张，得4分；
           若是两对，得3分；
           若是对子，得2分；
           若是散牌，得1分
        """
        if self.is_straight_flush():
            return 7
        elif self.is_flush():
            return 6
        elif self.is_straight():
            return 5
        elif isinstance(self.is_three_of_a_kind(), str):
            return 4
        elif isinstance(self.is_two_pairs(), list):
            return 3
        elif isinstance(self.is_one_pairs(), str):
            return 2
        else:
            return 1


def my_cmp_of_two(white, black):
    if white > black:
        return 'White wins'
    elif white < black:
        return 'Black wins'
    else:
        return 'Tie'


def my_cmp_of_all(white, black):
    for white.card, black.card in zip(white.cards[::-1], black.cards[::-1]):
        tmp_result = my_cmp_of_two(white.card[0], black.card[0])
        if tmp_result != 'Tie':
            return tmp_result
    return 'Tie'


class TexasHoldEmPoker:

    @staticmethod
    def result(white, black):
        white.score = white.get_score()
        black.score = black.get_score()
        if white.score > black.score:
            return 'White wins'
        elif black.score > white.score:
            return 'Black wins'
        else:
            if white.score == 7 or white.score == 5:
                if not white.cards[4][0] == black.cards[4][0] == chr(62):
                    return my_cmp_of_two(white.cards[4][0], black.cards[4][0])
                return my_cmp_of_all(white, black)
            elif white.score == 6:
                return my_cmp_of_all(white, black)
            elif white.score == 4 or white == 2:
                white.card = white.is_three_of_a_kind()
                black.card = black.is_three_of_a_kind()
                if my_cmp_of_two(white.card, black.card) == 'Tie':
                    return my_cmp_of_all(white, black)
                return 'Tie'
            elif white.score == 3:
                white.card = white.is_two_pairs()
                black.card = black.is_two_pairs()
                first_pair_result = my_cmp_of_two(white.card[1], black.card[1])
                second_pair_result = my_cmp_of_two(white.card[0], black.card[0])
                if first_pair_result == 'Tie' and second_pair_result == 'Tie':
                    return my_cmp_of_all(white, black)
                return first_pair_result if first_pair_result != 'Tie' else second_pair_result
            elif white.score == 1:
                return my_cmp_of_all(white, black)
