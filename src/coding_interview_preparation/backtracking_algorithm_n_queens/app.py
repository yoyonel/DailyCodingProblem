"""

"""
from functools import partial
from itertools import permutations
from matplotlib import pyplot
import time
import timeit
from typing import Iterator, Tuple


def handle_return(generator, func):
    """
    https://stackoverflow.com/questions/34073370/best-way-to-receive-the-return-value-from-a-python-generator
    https://www.python.org/dev/peps/pep-0380/

    :param generator:
    :param func:
    :return:
    """
    returned = yield from generator
    func(returned)


def wrapper_timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print(f'{method.__name__}  {(te - ts) * 1000} ms')
        return result
    return timed


def find_queens_placements_with_permutations(n: int) -> Iterator[Tuple[int, int]]:
    """
    https://en.wikipedia.org/wiki/Eight_queens_puzzle

    (Naive) Solution with permutations and generator

    :param n:
    :return:
    """
    metric_ops = 0

    # loop on all permutations
    # and filter them
    for p_q in permutations(range(n), n):
        on_diag = False
        for q_col, q_row in enumerate(p_q[:-1]):
            # loop through the rest of queens (next columns)
            for o_q_col, o_q_row in enumerate(p_q[q_col + 1:], start=1):
                # on diag of 'root' queen (q_col, q_row) ?
                on_diag = (q_row - o_q_col) == o_q_row or (q_row + o_q_col) == o_q_row
                metric_ops += 1
                if on_diag:
                    break
            # if one other queen in opposition with the root queen, abort the mission :p
            if on_diag:
                break
        # if no queens on oppositions return/send this queens placement
        if not on_diag:
            yield p_q

    return metric_ops


def find_queens_placements_with_backtracking(n: int):
    """

    :param n:
    :return:
    """
    metrics = {'nb_ops' : 0}

    queens = []
    all_queens_placements = []

    def isSafe(row, col) -> bool:
        for r, c in queens:
            if r == row:
                return False
            if abs(r - row) == abs(c - col):
                return False
        return True

    def placeQueens(col: int):
        if col >= n:
            all_queens_placements.append(queens.copy())
            return False
        row = 0
        while row < n:
            metrics['nb_ops'] += 1
            if isSafe(row, col):
                queens.append([row, col])
                if placeQueens(col+1):
                    return True
                queens.pop()
            row += 1
        return False

    placeQueens(0)
    for queens_placement in all_queens_placements:
        yield queens_placement

    return metrics


def plotTC(fn, nMin, nMax, nInc, nTests, label=""):
    """
    Run timer and plot time complexity
    """
    x = []
    y = []
    for i in range(nMin, nMax, nInc):
        N = i
        testNTimer = timeit.Timer(partial(fn, N))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    return pyplot.plot(x, y, 'o', label=label)


def main():
    def show_return(value):
        print(f'[METRIC] Number of operations: {value}')

    n = 10

    @wrapper_timeit
    def compute_with_permutations():
        gen_queens_placements = handle_return(find_queens_placements_with_permutations(n), show_return)
        for id_solution, queens_placement in enumerate(gen_queens_placements, 1):
            # print(f"#{id_solution}: {queens_placement}")
            pass
        print(f"Nb queens placements found with n={n} => {id_solution}")

    print("Compute with permutations")
    compute_with_permutations()

    print()

    @wrapper_timeit
    def compute_with_backtracking():
        gen_queens_placements = handle_return(find_queens_placements_with_backtracking(n), show_return)
        for id_solution, queens_placement in enumerate(gen_queens_placements, 1):
            # print(f"#{id_solution}: {[q[0] for q in queens_placement]}")
            pass
        print(f"Nb queens placements found with n={n} => {id_solution}")

    print("Compute with backtracking")
    compute_with_backtracking()

    # nTests = 10
    # testNTimer = timeit.Timer(partial(lambda n: list(find_queens_placements_with_backtracking(n)), n))
    # t = testNTimer.timeit(number=nTests)
    # print(t)

    # p1 = plotTC(lambda n: list(find_queens_placements_with_backtracking(n)), 2, n, 1, 10, label="with backtracking")
    # p2 = plotTC(lambda n: list(find_queens_placements_with_permutations(n)), 2, n, 1, 10, label="with permutations")
    # pyplot.legend()

    pyplot.show()

if __name__ == '__main__':
    main()
