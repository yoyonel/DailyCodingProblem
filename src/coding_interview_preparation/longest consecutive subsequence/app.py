"""
Given an array of integers,
find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers,
the consecutive numbers can be in any order.
"""
from typing import List


def find_length_of_longest_subsequence(arr: List[int]) -> int:
    # O(n) - O(n)
    set_hash = {
        v: True
        for v in arr
    }

    max_length = 0
    # nb_popitem = 0
    # max -> O(n)
    while set_hash:
        # get an item (integer) from hash map
        v = set_hash.popitem()[0]
        # nb_popitem += 1

        cur_length = 1

        # find all consecutive items in the left (optim: and remove them)
        i = v - 1
        while i in set_hash:
            del set_hash[i]
            cur_length += 1
            i -= 1
        # find all consecutive items in the right (optim: and remove them)
        i = v + 1
        while i in set_hash:
            del set_hash[i]
            cur_length += 1
            i += 1
        # update the length of the longest sub-sequence found
        max_length = max(max_length, cur_length)
    # print(f"nb_popitem={nb_popitem}")

    return max_length


def main():
    arr = [1, 9, 3, 10, 4, 20, 2]
    expected_output = 4
    assert find_length_of_longest_subsequence(arr) == expected_output

    arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    expected_output = 5
    assert find_length_of_longest_subsequence(arr) == expected_output


if __name__ == '__main__':
    main()
