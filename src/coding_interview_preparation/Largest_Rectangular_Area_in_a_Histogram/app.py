"""
I.
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars.
For simplicity, assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}.
The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)

II.
Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s.

Input :   0 1 1 0
          1 1 1 1
          1 1 1 1
          1 1 0 0

Output :  1 1 1 1
          1 1 1 1
"""
from typing import Any, List


def getMaxAreaFromHisto(hist: List[Any]) -> int:
    """

    :param hist:
    :return:
    """
    len_hist = len(hist)

    # Create an empty stack. The stack holds indexes
    # of hist[] array. The bars stored in stack are
    # always in increasing order of their heights.
    s = []  # type: List[Any]

    # Initialize max area
    max_area = 0

    # Run through all bars of given histogram
    i = 0

    def isNotEmpty(s: List[Any]) -> bool:
        return s

    def isEmpty(s: List[Any]) -> bool:
        return not s

    def getTop(s: List[Any]) -> Any:
        return s[-1]

    while (i < len_hist) or isNotEmpty(s):
        # If this bar is higher than the bar on top stack, push it to stack
        if (i < len_hist) and (isEmpty(s) or hist[getTop(s)] <= hist[i]):
            s.append(i)
            i += 1
        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with stack 
        # top as the smallest (or minimum height) bar. 
        # 'i' is 'right index' for the top and element 
        # before top in stack is 'left index'
        else:
            tp = s.pop()  # store the top index

            # Calculate the area with hist[tp] stack as smallest bar
            area_with_top = hist[tp] * (i if isEmpty(s) else (i - 1) - getTop(s))

            # update max area, if needed
            max_area = max(max_area, area_with_top)

    return max_area


# Returns area of the largest rectangle with all 1s in A[][]
def maxRectangle(A: List[List[Any]]) -> Any:
    # Calculate area for first row and initialize it as
    # result
    result = getMaxAreaFromHisto(A[0])

    # iterate over row to find maximum rectangular area
    # considering each row as histogram
    for id_row, row in enumerate(A[1:], start=1):
        for id_col, col in enumerate(row):
            # if A[i][j] is 1 then add A[i -1][j]
            if col == 1:
                A[id_row][id_col] += A[id_row - 1][id_col]

        # Update result if area with current row (as last row)
        # of rectangle) is more
        result = max(result, getMaxAreaFromHisto(A[id_row]))

    return result


def main():
    hist = [6, 2, 5, 4, 5, 1, 6]
    print(f"For hist={hist} -> Maximum area is {getMaxAreaFromHisto(hist)}")

    hist = [2, 3, 1, 4, 5, 4, 2]
    print(f"For hist={hist} -> Maximum area is {getMaxAreaFromHisto(hist)}")

    hist = [2, 2, 1, 2, 2]
    print(f"For hist={hist} -> Maximum area is {getMaxAreaFromHisto(hist)}")

    A = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]
    ]
    print(f"Maximum rectangle area is {maxRectangle(A)}")


if __name__ == '__main__':
    main()
