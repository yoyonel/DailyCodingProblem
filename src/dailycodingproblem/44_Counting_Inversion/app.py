"""
https://www.cp.eng.chula.ac.th/~piak/teaching/algo/algo2008/count-inv.htm

"""
from typing import List


def merge_and_count(ll: List[int], lr: List[int]) -> (int, List[int]):
    """

    :param ll:
    :param lr:
    :return:

    >>> merge_and_count([1, 2, 4], [3, 5])
    (1, [1, 2, 3, 4, 5])

    >>> merge_and_count([1, 2, 6], [3, 5])
    (2, [1, 2, 3, 5, 6])

    """
    result = []
    count = 0
    l_ll = len(ll)
    while ll and lr:
        val_ll = ll.pop(0)  # pop left
        val_lr = lr.pop(0)  # pop left

        if val_ll > val_lr:
            ll.insert(0, val_ll)  # add left
            count += l_ll
            result.append(val_lr)
        else:
            l_ll -= 1
            lr.insert(0, val_lr)  # add left
            result.append(val_ll)
    result += ll
    result += lr
    return count, result


def wrapper_sort_and_count(l: List[int]):
    if len(l) <= 1:
        return 0, l
    else:
        mid = len(l) // 2
        ll, lr = l[:mid], l[mid:]
        (r_ll, ll) = wrapper_sort_and_count(ll)
        (r_lr, lr) = wrapper_sort_and_count(lr)
        (r, l) = merge_and_count(ll, lr)
        return r_ll + r_lr + r, l


def sort_and_count(l: List[int]) -> int:
    return wrapper_sort_and_count(l)[0]


def main():
    assert sort_and_count([2, 4, 1, 3, 5]) == 3
    assert sort_and_count([5, 4, 3, 2, 1]) == 10


if __name__ == '__main__':
    main()
