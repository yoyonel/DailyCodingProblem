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
    # longest substring (found)
    lss = ""
    # current longest substring
    c_lss = ""
    # current list of characters for the current longest substring
    c_c = []

    i = 0
    for i, c in enumerate(s):
        # current character is in list of characters of the current substring ?
        if c in c_c:
            # if yes, increase/update current substring
            c_lss += c
        else:
            # else
            # Can we add the new character in the current substring ?
            if len(c_c) < k:
                # if yes: increase/updating the current substring
                c_lss += c
            else:
                # else => compare the current result (substring) & start a new substring research
                # compare the current substring with the longest substring found as far
                # Current substring is larger ?
                if len(c_lss) > len(lss):
                    # if yes: update the longest substring
                    lss = c_lss
                # in any case => start a new substring research
                # first element is: the last character of the previous current substring
                c_c = [c_lss[-1]]
                c_lss = c_lss[-1] + c
                # Early exit: at this moment, can we found a larger substring ?
                if (len(s) - i + len(c_lss)) <= len(lss):
                    break
            # add the new character in list of current character for substring
            c_c += [c]
    # perform a last comparaison for current substring
    if len(c_lss) > len(lss):
        lss = c_lss
    # print(len(s) - i - 1)
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
