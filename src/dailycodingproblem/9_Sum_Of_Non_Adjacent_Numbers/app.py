"""
largest sum of non-adjacent numbers of L=[2, 4, 6, 2, 5] -> 13
largest sum of non-adjacent numbers of L=[5, 1, 1, 5] -> 10
"""
from typing import List


def largest_sum_nonadjacents_numbers(L: List[int]) -> int:
    """

    :param L:
    :return:
    """
    cache = [0] * (len(L) + 2)

    i = 0
    for i, l in enumerate(L, start=2):
        cur_best_sum = l + cache[i-2]
        cache[i] = max(cur_best_sum, cache[i-1])
    return cache[i]


def largest_sum_nonadjacents_numbers_1(L: List[int]) -> int:
    """
    same as `largest_sum_nonadjacents_numbers` but with limited cache

    - speed: ~ O(|L|) = O(N) (N: size input)
    - memory: constant (k variables)

    :param L:
    :return:
    """
    cache_n2 = 0
    cache_n1 = 0
    best_sum = 0
    for l in L:
        best_sum = max(l + cache_n2, cache_n1)
        # update cache for next iteration
        cache_n2 = cache_n1
        cache_n1 = best_sum

    return best_sum


def main():
    L = [2, 4, 6, 2, 5]
    print(f"largest sum of non-adjacent numbers of L={L} -> {largest_sum_nonadjacents_numbers_1(L)}")

    L = [5, 1, 1, 5]
    print(f"largest sum of non-adjacent numbers of L={L} -> {largest_sum_nonadjacents_numbers_1(L)}")


if __name__ == '__main__':
    main()
