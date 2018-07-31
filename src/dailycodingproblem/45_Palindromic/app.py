"""
Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""
import logging


logger = logging.getLogger(__name__)


def find_longest_palindromic_contiguous_substring(s: str):
    """
    O(n^2) - O(1)

    :param s:
    :return:
    """

    logger.debug(f"input string: {s}")
    l_s = len(s)
    # result
    lpcs = 0
    lpcs_left = lpcs_right = 0

    def _find_lpcs(c_i: int, l_i: int, r_i: int):
        """
        Finding lpcs engine used for odd/even palindromic research

        :param c_i: current index
        :param l_i: left index
        :param r_i: right index
        :return:
        """
        # count expand step
        nb_expand_step = 1
        logger.debug(
            f"s[{c_i}]={s[c_i]}\n\ts[left={l_i}]: {s[l_i]} - s[right={r_i}]: {s[r_i]}")
        while (r_i < (l_s - 1)) and (l_i > 0) and (s[l_i] == s[r_i]):
            nb_expand_step += 1
            l_i -= 1
            r_i += 1
            logger.debug(f"\ts[left={l_i}]: {s[l_i]} - s[right={r_i}]: {s[r_i]}")
        logger.debug(f"Nb expand step: {nb_expand_step} -> {1 + nb_expand_step*2}")
        return 1 + nb_expand_step * 2, l_i, r_i

    # Consider all characters as a possible start center for a palindromic contiguous substring
    i = 1   # start at index=1 (backtrack oriented (for odd palindromic))
    while i < (l_s - 1):
        # odd palindromic
        # TODO: remove duplicate code for updating the result
        len_pcs, left, right = _find_lpcs(i, i - 1, i + 1)
        if len_pcs > lpcs:
            lpcs = len_pcs
            lpcs_left = left + 1 * (s[left] != s[right])
            lpcs_right = right - 1 * (s[left] != s[right])

        # even palindromic
        len_pcs, left, right = _find_lpcs(i, i - 1, i)
        # TODO: remove duplicate code for updating the result
        if len_pcs > lpcs:
            lpcs = len_pcs
            lpcs_left = left + 1 * (s[left] != s[right])
            lpcs_right = right - 1 * (s[left] != s[right])

        # next character
        i += 1

    # return substring of the longest palindromic contiguous
    return s[lpcs_left:lpcs_right+1]


def main():
    logging.basicConfig(
        format='%(message)s',
        level=logging.DEBUG,
    )
    tests = [
        ("bananas", "anana"),
        ("aabcdcb", "bcdcb"),
        ("totobaabtata", "baab"),
    ]
    for t_i, t_re in tests:
        logger.debug('#' * 80)
        assert t_re == find_longest_palindromic_contiguous_substring(t_i)
        logger.debug('#'*80)


if __name__ == '__main__':
    main()
