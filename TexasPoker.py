def who_win(black, white):
    # 输入
    result = None
    black_values, black_kinds = cards2list(black)
    white_values, white_kinds = cards2list(white)
    black_values, black_kinds = sort(black_values, black_kinds)
    white_values, white_kinds = sort(white_values, white_kinds)
    black_rank = rank(black_values, black_kinds)
    white_rank = rank(white_values, white_kinds)

    # 判断牌的等级，等级不同等级大的赢
    if black_rank > white_rank:
        result = 0
    elif black_rank < white_rank:
        result = 1
    # 牌的等级相同时的比大小
    else:
        if black_rank == 0:
            result = rank_0(black_values, white_values)
        elif black_rank == 1:
            result = rank_1(black_values, white_values)
        elif black_rank == 2:
            result = rank_2(black_values, white_values)
        elif black_rank == 3:
            result = rank_3(black_values, white_values)
        elif black_rank == 4:
            result = rank_4(black_values, white_values)
        elif black_rank == 5:
            result = rank_5(black_values, white_values)
        elif black_rank == 6:
            result = rank_6(black_values, white_values)
        elif black_rank == 7:
            result = rank_7(black_values, white_values)
        elif black_rank == 8:
            result = rank_8(black_values, white_values)
    # 输出结果
    if result == 0:
        return "Black wins"
    elif result == 1:
        return "White wins"
    else:
        return "Tie"


# 输入
def cards2list(card):
    values = []
    kinds = []
    cards = card.split()
    for card in cards:
        values.append(card[0])
        kinds.append(card[1])
    return values, kinds


# 两张牌点数比大小
def higher_than(value1, value2):
    order = "23456789TJQKA"
    if order.index(value1) > order.index(value2):
        return 1
    if order.index(value1) < order.index(value2):
        return 0
    if order.index(value1) == order.index(value2):
        return 2


# 从大到小排序
def sort(values, types):
    for i in range(5):
        for j in range(i + 1, 5):
            if higher_than(values[i], values[j]) == 0:
                values[i], values[j] = values[j], values[i]
                types[i], types[j] = types[j], types[i]
    return values, types


# 同花
def flush(values, types):
    if len(set(types)) == 1:
        return True
    return False


# 顺子
def straight(values, types):
    order = "23456789TJQKA"
    flag = 0
    for i in range(4):
        if order.index(values[i]) != order.index(values[i + 1]) + 1:
            return False
    return True


# m之后的n张牌点数相同
def same_value(values, m, n):
    for i in range(m + 1, m + n):
        if values[i] != values[m]:
            return False
    return True


# 牌的级别
def rank(values, types):
    if flush(values, types) and straight(values, types):
        return 8
    if same_value(values, 0, 4) or same_value(values, 1, 4):
        return 7
    if same_value(values, 0, 3) and same_value(values, 3, 2):
        return 6
    if same_value(values, 0, 2) and same_value(values, 2, 3):
        return 6
    if flush(values, types):
        return 5
    if straight(values, types):
        return 4
    if same_value(values, 0, 3) or same_value(values, 1, 3) or same_value(values, 2, 3):
        return 3
    if same_value(values, 0, 2) and same_value(values, 2, 2):
        return 2
    if same_value(values, 0, 2) and same_value(values, 3, 2):
        return 2
    if same_value(values, 1, 2) and same_value(values, 3, 2):
        return 2
    if (
        same_value(values, 0, 2)
        or same_value(values, 1, 2)
        or same_value(values, 2, 2)
        or same_value(values, 3, 2)
    ):
        return 1
    return 0

# 频数统计
def sta(values):
    new_values = []
    numbers = []
    for value in values:
        if value not in new_values:
            new_values.append(value)
            numbers.append(1)
        else:
            numbers[new_values.index(value)] += 1
    for i in range(len(new_values)):
        for j in range(i + 1, len(new_values)):
            if numbers[i] < numbers[j]:
                new_values[i], new_values[j] = new_values[j], new_values[i]
                numbers[i], numbers[j] = numbers[j], numbers[i]
            if numbers[i] == numbers[j] and higher_than(new_values[i], new_values[j]) == 0:
                new_values[i], new_values[j] = new_values[j], new_values[i]
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return new_values, numbers

# 同级别比大小
# 0.散牌：不符合其他任何规则的五张牌。 比较最大一张牌的大小，如果相同，比较第二大的牌的牌点数，如果五张牌的牌点数都相同，则为平局。
def rank_0(black_values, white_values):
    for i in range(5):
        if higher_than(black_values[i], white_values[i]) == 1:
            return 0
        if higher_than(black_values[i], white_values[i]) == 0:
            return 1
        if higher_than(black_values[i], white_values[i]) == 2:
            continue
    return 2

# 1. 对子：有两张同样大小的牌片。 比较两张大小一样的牌的牌点数，如果相同，依次比较剩余的三张牌大小。若大小都相同，则为平局。
def rank_1(black_values, white_values):
    sta_black_values, num_black_values = sta(black_values)
    sta_white_values, num_white_values = sta(white_values)
    if higher_than(sta_black_values[0], sta_white_values[0]) == 1:
        return 0
    if higher_than(sta_black_values[0], sta_white_values[0]) == 0:
        return 1
    if higher_than(sta_black_values[0], sta_white_values[0]) == 2:
        for i in range(1,4):
            if higher_than(black_values[i], white_values[i]) == 1:
                return 0
            if higher_than(black_values[i], white_values[i]) == 0:
                return 1
            if higher_than(black_values[i], white_values[i]) == 2:
                continue
    return 2


# 2. 两对：有两个对子牌。 比较大对子的大小，若相同，比较小对子的大小，若还相同，比较单张牌的大小，若还相同，则为平局。
def rank_2(black_values, white_values):
    sta_black_values, num_black_values = sta(black_values)
    sta_white_values, num_white_values = sta(white_values)
    if higher_than(sta_black_values[0], sta_white_values[0]) == 1:
        return 0
    if higher_than(sta_black_values[0], sta_white_values[0]) == 0:
        return 1
    if higher_than(sta_black_values[1], sta_white_values[1]) == 1:
        return 0
    if higher_than(sta_black_values[1], sta_white_values[1]) == 0:
        return 1
    if higher_than(sta_black_values[0], sta_white_values[0]) == 2:
        if higher_than(black_values[2], white_values[2]) == 1:
            return 0
        if higher_than(black_values[2], white_values[2]) == 0:
            return 1
        if higher_than(black_values[2], white_values[2]) == 2:
            return 2
    return 2


# 3. 三条：有三张同样大小的牌片。 比较三张大小一样的牌的牌点数大小。
def rank_3(black_values, white_values):
    sta_black_values, num_black_values = sta(black_values)
    sta_white_values, num_white_values = sta(white_values)
    if higher_than(sta_black_values[0], sta_white_values[0]) == 1:
        return 0
    if higher_than(sta_black_values[0], sta_white_values[0]) == 0:
        return 1
    if higher_than(sta_black_values[0], sta_white_values[0]) == 2:
        return 2


# 4. 顺子：五张相连的牌。 比较最大的牌点数。若大小都相同，则为平局。
def rank_4(black_values, white_values):
    if higher_than(black_values[0], white_values[0]) == 1:
        return 0
    if higher_than(black_values[0], white_values[0]) == 0:
        return 1
    if higher_than(black_values[0], white_values[0]) == 2:
        return 2


# 5. 同花：五张牌的花色相同。 按照散排规则比较大小。
def rank_5(black_values, white_values):
    for i in range(5):
        if higher_than(black_values[i], white_values[i]) == 1:
            return 0
        if higher_than(black_values[i], white_values[i]) == 0:
            return 1
        if higher_than(black_values[i], white_values[i]) == 2:
            continue


# 6. 葫芦：三条+对子。 比较三张大小一样的牌的牌点数。
def rank_6(black_values, white_values):
    sta_black_values, num_black_values = sta(black_values)
    sta_white_values, num_white_values = sta(white_values)
    if higher_than(sta_black_values[0], sta_white_values[0]) == 1:
        return 0
    if higher_than(sta_black_values[0], sta_white_values[0]) == 0:
        return 1
    if higher_than(sta_black_values[0], sta_white_values[0]) == 2:
        return 2


# 7. 铁支：有四张同样大小的牌片。 比较四张大小一样的牌的牌点数。
def rank_7(black_values, white_values):
    sta_black_values, num_black_values = sta(black_values)
    sta_white_values, num_white_values = sta(white_values)
    if higher_than(sta_black_values[0], sta_white_values[0]) == 1:
        return 0
    if higher_than(sta_black_values[0], sta_white_values[0]) == 0:
        return 1
    if higher_than(sta_black_values[0], sta_white_values[0]) == 2:
        return 2


# 8. 同花顺：同一种花色的顺子。 比较最大的牌的牌的大小。若大小都相同，则为平局。
def rank_8(black_values, white_values):
    if higher_than(black_values[0], white_values[0]) == 1:
        return 0
    if higher_than(black_values[0], white_values[0]) == 0:
        return 1
    if higher_than(black_values[0], white_values[0]) == 2:
        return 2


if __name__ == "__main__":
    pass
