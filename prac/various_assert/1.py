


import random


def get_none():
    """ Noneを返す
    """
    return None


def get_num():
    """ 0 - 9 の整数を返す
    """
    return random.randint(0, 9)


def get_list():
    """ 長さが5の、1 - 9 のランダムな値を含むリストを返す。ただし 0 は必ず含む
    """
    candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return [random.choice(candidates) for _ in range(4)] + [0]


def raise_value_error():
    raise ValueError