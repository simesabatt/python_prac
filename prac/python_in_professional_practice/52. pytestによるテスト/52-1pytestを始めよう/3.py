from leap import isleap


def test_isleap_1():
    assert not isleap(2019)


def test_isleap_2():
    assert isleap(2020)


def test_isleap_3():
    assert not isleap(1900)


def test_isleap_4():
    assert isleap(2000)



# def isleap(year):
#     if year % 4:  # 4で割り切れなければうるう年でない
#         return False
#     elif year % 100:  # 4の倍数で100で割り切れなければうるう年である
#         return True
#     elif year % 400:  # 100の倍数で400で割り切れなければうるう年でない
#         return False
#     else:  # 400の倍数はうるう年である
#         return True