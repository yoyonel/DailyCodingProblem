"""

"""
from collections import defaultdict
from functools import reduce
import random


def rand5():
    return random.randint(1, 5)


def rand7():
    """
    non deterministic
    :return:
    """
    s = 5 * rand5() + rand5()
    while s > 20:
        s = 5 * rand5() + rand5()

    return s % 7


def rand7_v2():
    """
    deterministic

    :return:
    """
    return (rand5() + rand5() * 10 + rand5() * 100 * rand5() * 1000 + rand5() * 10000 + rand5() * 100000) % 7 + 1


def rand7_v3():
    """

    :return:
    """
    n = rand5() + 6 * (
                rand5() + 6 * (rand5() + 6 * (rand5() + 6 * (rand5() + 6 * (rand5() + 6 * (rand5() + 6 * (rand5())))))))
    return n % 8
    # return rand5() + reduce(lambda x, y: x + 6 * y, [rand5() for _ in range(7)]) % 8


if __name__ == '__main__':
    d = defaultdict(int)
    for e in [rand7() for _ in range(10000)]:
        d[e] += 1
    print(d)

    d = defaultdict(int)
    for e in [rand7_v2() for _ in range(10000)]:
        d[e] += 1
    print(d)

    d = defaultdict(int)
    for e in [rand7_v3() for _ in range(10000)]:
        d[e] += 1
    print(d)
