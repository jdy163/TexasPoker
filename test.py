import TexasPoker
import pytest

class TestClass:
    # 散牌 vs 散牌
    def test_1(self):
        assert TexasPoker.who_win("2H 3D 5S 9C KD","2C 3H 4S 8C AH") == "White wins"
    # 葫芦 vs 同花
    def test_2(self):
        assert TexasPoker.who_win("2H 4S 4C 2D 4H","2S 8S AS QS 3S") == "Black wins"
    # 散牌 vs 散牌
    def test_3(self):
        assert TexasPoker.who_win("2H 3D 5S 9C KD","2C 3H 4S 8C KH") == "Black wins"
    # 散牌 vs 散牌
    def test_4(self):
        assert TexasPoker.who_win("2H 3D 5S 9C KD","2D 3H 5C 9S KH") == "Tie"
    # 同花顺 vs 同花顺
    def test_5(self):
        assert TexasPoker.who_win("9H TH JH QH KH","2D 3D 6D 5D 4D") == "Black wins"
    # 同花顺 vs 散牌
    def test_6(self):
        assert TexasPoker.who_win("9D TH JH QH KH","2D KD QH TD 4D") == "Black wins"
    # 对子 vs 对子
    def test_7(self):
        assert TexasPoker.who_win("9D TH 9H QH KH","9D KD QH 9D 4D") == "Black wins"
    # 对子 vs 对子
    def test_8(self):
        assert TexasPoker.who_win("9D TH 9H QH KH","8D KD QH 8D 4D") == "Black wins"
    # 双对 vs 对对
    def test_9(self):
        assert TexasPoker.who_win("9D 9H TH TH KH","9D 9D 8H 8D 4D") == "Black wins"
    # 铁支 vs 铁支
    def test_10(self):
        assert TexasPoker.who_win("9D 9H 9H 9H KH","8D 8D 8H 8D 7D") == "Black wins"
    # 三条 vs 三条
    def test_11(self):
        assert TexasPoker.who_win("9D TH 9H 9H KH","8D 8D QH 9D 8D") == "Black wins"