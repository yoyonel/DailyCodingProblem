"""
@ level=1/4 - with X={1, 2} -> ways to climb: [[1]]
@ level=2/4 - with X={1, 2} -> ways to climb: [[1, 1], [2]]
@ level=3/4 - with X={1, 2} -> ways to climb: [[1, 1, 1], [2, 1], [1, 2]]
@ level=4/4 - with X={1, 2} -> ways to climb: [[1, 1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [2, 2]]
@ level=1/4 - with X={1, 3, 5} -> ways to climb: [[1]]
@ level=2/4 - with X={1, 3, 5} -> ways to climb: [[1, 1]]
@ level=3/4 - with X={1, 3, 5} -> ways to climb: [[1, 1, 1], [3]]
@ level=4/4 - with X={1, 3, 5} -> ways to climb: [[1, 1, 1, 1], [3, 1], [1, 3]]
"""
from collections import deque
from typing import Generator, Iterable


def find_all_ways_to_climb_staircases(N: int, X: Iterable[int]) -> Generator:
    """

    :param N:
    :param X:
    :return:
    """
    cache = [[[]]] * (N + 1)
    # 0 -> 1 way={[0]} ~ {[]}
    # Start computation at level/N=1
    for n in range(1, N + 1):
        cache[n] = [
            way + [x]   # Solution way format: Old/Previous way + New step
            for x in X if (n - x) >= 0
            for way in cache[n - x]
        ]
        yield cache[n]


def find_ways_to_climb_staricase(N: int, X: Iterable[int]) -> Iterable:
    """

    :param N:
    :param X:
    :return:
    """
    # https://stackoverflow.com/questions/2138873/cleanest-way-to-get-last-item-from-python-iterator
    return deque(find_all_ways_to_climb_staircases(N, X), maxlen=1).pop()


def main():
    N = 4
    X = {1, 2}
    for n, ways in enumerate(find_all_ways_to_climb_staircases(N, X), start=1):
        print(f"@ level={n}/{N} - with X={X} -> ways to climb: {ways}")
    print()

    X = {1, 3, 5}
    for n, ways in enumerate(find_all_ways_to_climb_staircases(N, X), start=1):
        print(f"@ level={n}/{N} - with X={X} -> ways to climb: {ways}")
    print()

    X = {1, 2}
    print(f"@ level={N} - with X={X} -> ways to climb: {find_ways_to_climb_staricase(N, X)}")


if __name__ == '__main__':
    main()
