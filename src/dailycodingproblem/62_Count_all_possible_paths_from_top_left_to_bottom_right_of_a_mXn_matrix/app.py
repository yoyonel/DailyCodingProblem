"""
There is an N by M matrix of zeroes.
Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner.
You can only move right or down.

0 0
0 0
=> 2

0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
=> 70

$ python app.py
→ → → ↓
. . . ↓
. . . ↓
. . . ↓
. . . x

→ → ↓ .
. . → ↓
. . . ↓
. . . ↓
. . . x

...


# online Python3 IDE
Count all possible paths from top left to bottom right of a mXn matrix (Python v3.6.2)
http://tpcg.io/H2QIsx
"""
import functools
from itertools import combinations
import operator
from typing import Iterator, List

product = functools.partial(functools.reduce, operator.mul)


def naive_factorial(n: int) -> int:
    """Naive implementation of factorial: product([1, ..., n])

    https://bugs.python.org/issue8692
    https://bugs.python.org/file17320/factorial4.py
    http://www.luschny.de/math/factorial/binarysplitfact.html

    >>> naive_factorial(4)
    24
    """
    return product(range(1, n + 1), 1)


def number_of_paths(m: int, n: int) -> int:
    """
    Returns count of possible paths to reach cell
    at row number m and column number n from the
    topmost leftmost cell (cell at 1, 1)

    :param m: number of rows
    :param n: number of columns
    :return: number of paths

    >> numberOfPaths(2, 2)
    2
    >> numberOfPaths(5, 5)
    70
    """
    m = m - 1
    n = n - 1
    return naive_factorial(m + n) // naive_factorial(m) // naive_factorial(n)


# http://xahlee.info/comp/unicode_arrows.html
def iterate_on_all_paths(
        m: int,
        n: int,
        right_chr: str = '→',
        down_chr: str = '↓',
) -> Iterator[List[str]]:
    """

    :param m:
    :param n:
    :param right_chr:
    :param down_chr:
    :return:

    >>> list(iterate_on_all_paths(3, 3))
    [\
['→', '→', '↓', '↓'], ['→', '↓', '→', '↓'], ['→', '↓', '↓', '→'], \
['↓', '→', '→', '↓'], ['↓', '→', '↓', '→'], ['↓', '↓', '→', '→']]

    >>> list(iterate_on_all_paths(4, 4))
    [\
['→', '→', '→', '↓', '↓', '↓'], ['→', '→', '↓', '→', '↓', '↓'], ['→', '→', '↓', '↓', '→', '↓'], \
['→', '→', '↓', '↓', '↓', '→'], ['→', '↓', '→', '→', '↓', '↓'], ['→', '↓', '→', '↓', '→', '↓'], \
['→', '↓', '→', '↓', '↓', '→'], ['→', '↓', '↓', '→', '→', '↓'], ['→', '↓', '↓', '→', '↓', '→'], \
['→', '↓', '↓', '↓', '→', '→'], ['↓', '→', '→', '→', '↓', '↓'], ['↓', '→', '→', '↓', '→', '↓'], \
['↓', '→', '→', '↓', '↓', '→'], ['↓', '→', '↓', '→', '→', '↓'], ['↓', '→', '↓', '→', '↓', '→'], \
['↓', '→', '↓', '↓', '→', '→'], ['↓', '↓', '→', '→', '→', '↓'], ['↓', '↓', '→', '→', '↓', '→'], \
['↓', '↓', '→', '↓', '→', '→'], \
['↓', '↓', '↓', '→', '→', '→']]

    """
    if m <= 0:
        raise ValueError(f'm(={m}) must be > 0')
    if n <= 0:
        raise ValueError(f'n(={n}) must be > 0')

    m = m - 1
    n = n - 1

    def _iterate_on_all_rights_mouvements():
        for ids_set_to_right in combinations(range(m + n), n):
            yield ids_set_to_right

    def _generate_path_from_rights_mouvements(id_rm: Iterator[List[int]]) -> Iterator[List[str]]:
        for ids_set_to_right in id_rm:
            path = [down_chr for _ in range(m + n)]
            for id_to_set_to_right in ids_set_to_right:
                path[id_to_set_to_right] = right_chr
            yield path

    return _generate_path_from_rights_mouvements(_iterate_on_all_rights_mouvements())
    # yield ids_set_to_right


def build_matrix_with_path(
        m: int,
        n: int,
        path: List[str],
        chr_empty: str = '0',
        chr_dst: str = 'X',
        right_chr: str = '→',
) -> List[List[str]]:
    """

    :param m:
    :param n:
    :param path:
    :param chr_empty:
    :param chr_dst:
    :param right_chr:
    :return:

    >>> build_matrix_with_path(3, 3, next(iterate_on_all_paths(3, 3)))
    [['→', '→', '↓'], ['0', '0', '↓'], ['0', '0', 'X']]
    """
    matrix_with_path = [[chr_empty for _ in range(n)] for _ in range(m)]
    cur_pos = [0, 0]
    for mouvement in path:
        matrix_with_path[cur_pos[1]][cur_pos[0]] = mouvement
        cur_pos[mouvement != right_chr] += 1
    matrix_with_path[cur_pos[1]][cur_pos[0]] = chr_dst
    return matrix_with_path


def print_matrix_of_all_paths(m: int, n: int, chr_empty: str='◯', chr_dst: str='x'):
    """

    :param m:
    :param n:
    :param chr_empty:
    :param chr_dst:
    :return:
    """
    for path in iterate_on_all_paths(m, n):
        matrix_with_path = build_matrix_with_path(m, n, path, chr_empty, chr_dst)
        for row in matrix_with_path:
            print(" ".join(row))
        print()


def main():
    assert number_of_paths(2, 2) == 2
    assert number_of_paths(5, 5) == 70

    print_matrix_of_all_paths(m=5, n=4, chr_empty='◯', chr_dst='⚫')

    print(number_of_paths(13, 13))


if __name__ == '__main__':
    main()
