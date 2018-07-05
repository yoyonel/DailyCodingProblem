"""

"""
from functools import lru_cache
nb_rec = 0


def count_sets(arr, total):
    return rec(arr, total, len(arr) - 1)


def rec(arr, total, i):
    @lru_cache()
    def cached_rec(_total, _i):
        global nb_rec
        nb_rec += 1
        if _total == 0:
            return 1
        elif _total < 0:
            return 0
        elif _i < 0:
            return 0
        else:
            return cached_rec(_total, _i-1) + cached_rec(_total - arr[_i], _i-1)
    return cached_rec(total, i)


def count_sets_without_cache(arr, total):
    return rec_without_cache(arr, total, len(arr) - 1)


def rec_without_cache(arr, total, i):
    global nb_rec
    nb_rec += 1
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    else:
        return rec_without_cache(arr, total, i-1) + rec_without_cache(arr, total - arr[i], i-1)


def main():
    global nb_rec

    arr = [10, 2, 4, 6]
    expected_result = 2     # [2, 4, 10] & [6, 10]
    assert count_sets(arr, 16) == expected_result
    nb_rec_with_cache = nb_rec

    nb_rec = 0
    assert count_sets_without_cache(arr, 16) == expected_result
    nb_rec_without_cache = nb_rec

    assert nb_rec_with_cache < nb_rec_without_cache


if __name__ == '__main__':
    main()
