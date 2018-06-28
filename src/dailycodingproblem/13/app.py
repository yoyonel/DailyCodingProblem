"""

"""


def find_longest_substring(s: str, k: int) -> str:
    """
    Speed: ~O(N)
    Memory: ~O(1)

    :param s:
    :param k:
    :return:
    """
    lss = ""
    c_lss = ""
    c_c = []
    c_nb_c = 0
    # TODO: add early exit with while loop (and "good" condition ;-))
    for c in s:
        if c in c_c:
            c_lss += c
        else:
            if c_nb_c < k:
                c_lss += c
                c_c += [c]
                c_nb_c += 1
            else:
                if len(c_lss) > len(lss):
                    lss = c_lss
                c_lss = c_lss[-1] + c
                c_c = [c_lss[-2], c_lss[-1]]
                c_nb_c = 2
    if len(c_lss) > len(lss):
        lss = c_lss
    return lss


def main():
    s = "abcba"
    k = 2
    assert find_longest_substring(s, k) == "bcb"

    s = "abcbabaab"
    k = 2
    assert find_longest_substring(s, k) == "babaab"

    s = "abcbabaab"
    k = 3
    assert find_longest_substring(s, k) == s

    s = "abcbadbaab"
    k = 3
    assert find_longest_substring(s, k) == "adbaab"


if __name__ == '__main__':
    main()
