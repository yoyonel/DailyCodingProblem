"""
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
"""
from typing import List


def compute_largest_sum_contiguous_subarray(a: List[int]) -> int:
    """

    :param a:
    :return:


    >>> compute_largest_sum_contiguous_subarray([34, -50, 42, 14, -5, 86])
    137
    >>> compute_largest_sum_contiguous_subarray([-5, -1, -8, -9])
    0
    """
    max_so_far = 0
    max_ending_here = 0

    for e in a:
        max_ending_here = max(0, max_ending_here + e)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def main():
    pass


if __name__ == '__main__':
    main()
