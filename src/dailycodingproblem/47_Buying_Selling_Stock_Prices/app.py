"""
This problem was asked by Facebook.
"""
import sys
from typing import List


def compute_maximum_profit(stock_prices: List[int]) -> int:
    """
    Given a array of numbers representing the stock prices of a company in chronological order,
    write a function that calculates the maximum profit you could have made from buying and selling that stock once.
    You must buy before you can sell it.

    For example, given [9, 11, 8, 5, 7, 10], you should return 5,
    since you could buy the stock at 5 dollars and sell it at 10 dollars.

    O(n) - O(1)

    :param stock_prices:
    :return:

    >>> compute_maximum_profit([9, 11, 8, 5, 7, 10])
    5
    """
    # O(1)
    best_deal = 0
    cur_buying = sys.maxsize
    cur_deal = 0

    # O(n + 1) ~ O(n)
    # Add a dummy element to update the result (best deal) with the last element (of stock prices list)
    for sp in stock_prices + [0]:
        if sp < cur_buying:
            # update the best dealing found as far
            best_deal = max(best_deal, cur_deal)
            # next search for best dealing
            cur_buying = sp
            cur_deal = 0
        else:
            # update the dealing for the current search
            cur_deal = max(sp - cur_buying, cur_deal)
    # return the best dealing found
    return best_deal


def test_compute_maximum_profit():
    tests = [
        ([9, 11, 8, 5, 7, 10], (10 - 5)),
        ([1, 2, 3, 4, 5, 6], (6 - 1)),
        ([6, 5, 4, 3, 2, 1], 0),
    ]
    for stock_prices, result_expected in tests:
        assert compute_maximum_profit(stock_prices) == result_expected


def main():
    test_compute_maximum_profit()


if __name__ == '__main__':
    main()
