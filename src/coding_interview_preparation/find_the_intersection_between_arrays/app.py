"""
Found intersections from 3 arrays (of integers) sorted.
+
Found intersections from k arrays (of integers) sorted.
"""
from typing import List


def find_intersections_arrays(arrs: List[List[int]]) -> List[int]:
    """

    :param arrs:
    :return:

    >>> arr1 = [2, 6, 9, 11, 13, 17]
    >>> arr2 = [3, 6, 7, 10, 13, 18]
    >>> arr3 = [4, 5, 6, 9, 11, 13]
    >>> find_intersections_arrays([arr1, arr2, arr3])
    [6, 13]

    """
    len_arrs = len(arrs)
    result = []
    i_arrs = [0] * len_arrs

    l_arrs = [len(arr) for arr in arrs]

    def OOB():
        """
        :return:
        """
        return all([i_arr < l_arr for i_arr, l_arr in zip(i_arrs, l_arrs)])

    while OOB():
        # all elements in arrays (at indidces) are equals
        if len(set([arr[i_arr] for arr, i_arr in zip(arrs, i_arrs)])) == 1:
            # add element to results
            result.append(arrs[0][i_arrs[0]])
            # update indices on all arrays
            i_arrs = [
                i_arr + 1
                for i_arr in i_arrs
            ]
        else:
            # search the indice (on array) to update
            id_arr = 0
            for id_arr, (arr0, arr1) in enumerate(zip(arrs[:-1], arrs[1:])):
                if arr0[i_arrs[id_arr]] < arr1[i_arrs[id_arr+1]]:
                    i_arrs[id_arr] += 1
                    break
            if id_arr == len_arrs - 2:
                i_arrs[-1] += 1
    return result


def find_intersections_3arrays(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    result = []
    i_arr1 = i_arr2 = i_arr3 = 0

    l_arr1 = len(arr1)
    l_arr2 = len(arr2)
    l_arr3 = len(arr3)

    def OOB():
        return i_arr1 < l_arr1 and i_arr2 < l_arr2 and i_arr3 < l_arr3

    while OOB():
        if arr1[i_arr1] == arr2[i_arr2] == arr3[i_arr3]:
            result.append(arr1[i_arr1])
            # update indices on all arrays
            i_arr1 += 1
            i_arr2 += 1
            i_arr3 += 1
        else:
            if arr1[i_arr1] < arr2[i_arr2]:
                i_arr1 += 1
            elif arr2[i_arr2] < arr3[i_arr3]:
                i_arr2 += 1
            else:
                i_arr3 += 1

    return result


def main():
    arr1 = [2, 6, 9, 11, 13, 17]
    arr2 = [3, 6, 7, 10, 13, 18]
    arr3 = [4, 5, 6, 9, 11, 13]

    expected_result = [6, 13]

    assert find_intersections_3arrays(arr1, arr2, arr3) == expected_result

    assert find_intersections_arrays([arr1, arr2, arr3]) == expected_result


if __name__ == '__main__':
    main()
