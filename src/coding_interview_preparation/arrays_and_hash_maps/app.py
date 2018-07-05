"""
Problem: You are given an array of repeating numbers.
All numbers repeat in an even way, except for one.
Find that odd occurring number.
"""


def main():
    entries = [1, 4, 6, 4, 1]
    expected_result = 6

    # tracking odd count of values
    map_odd_values = {}
    for v in entries:
        try:
            del map_odd_values[v]
        except KeyError:
            map_odd_values[v] = True

    assert list(map_odd_values.keys())[0] == expected_result


if __name__ == '__main__':
    main()
