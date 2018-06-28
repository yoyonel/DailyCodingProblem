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

    i = 0
    for i, c in enumerate(s):
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

                # Early exit
                if (len(s) - i + len(c_lss)) <= len(lss):
                    break
    if len(c_lss) > len(lss):
        lss = c_lss
    print(len(s) - i)
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

    s = "abbbbbbbbbbbbbaaaaacbadbaab"
    k = 2
    assert find_longest_substring(s, k) == "abbbbbbbbbbbbbaaaaa"


if __name__ == '__main__':
    main()
