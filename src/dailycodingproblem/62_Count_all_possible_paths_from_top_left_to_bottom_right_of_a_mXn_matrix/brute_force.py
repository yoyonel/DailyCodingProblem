"""

"""
# Python program to count all possible paths
# from top left to bottom right

o_numberOfPaths = 0


# function to return count of possible paths
# to reach cell at row number m and column
# number n from the topmost leftmost
# cell (cell at 1, 1)
def numberOfPaths(m, n):
    global o_numberOfPaths

    o_numberOfPaths += 1

    # If either given row number is first
    # or given column number is first
    if m == 1 or n == 1:
        return 1

    # If diagonal movements are allowed
    # then the last addition
    # is required.
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)


if __name__ == '__main__':
    # Driver program to test above function
    m = 13
    n = 13

    number_of_paths = numberOfPaths(m, n)

    print(f"numberOfPaths({m}, {n}) = {number_of_paths}")
    print(
        f"O(numberOfPaths({m}, {n})) = {o_numberOfPaths} == (numberOfPaths({m}, {n}) * 2 - 1) ? => {o_numberOfPaths == number_of_paths * 2 - 1}")
