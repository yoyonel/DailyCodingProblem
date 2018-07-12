"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""
from typing import Any, Dict, List, Optional


def is_well_formed(
        s: str,
        map_close_to_open_brackets: Optional[Dict[str, str]] = None
) -> bool:
    """
    O(k) - O(k')
    k: len of input string
    k': # open brackets (<= k)

    :param s:
    :param map_close_to_open_brackets
    :return:

    >>> is_well_formed("([])[]({})")
    True
    >>> is_well_formed("([)]")
    False
    >>> is_well_formed("((()")
    False
    >>> is_well_formed("(toto)")
    True
    """
    if not map_close_to_open_brackets:
        map_close_to_open_brackets = {'}': '{', ')': '(', ']': '['}

    def is_open_bracket(c: str) -> bool:
        return c in map_close_to_open_brackets.values()

    def is_close_bracket(c: str) -> bool:
        return c in map_close_to_open_brackets.keys()

    def get_open_bracket(cb: str) -> str:
        return map_close_to_open_brackets.get(cb, None)

    def get_top(stack: List[Any]) -> Any:
        return stack[-1]

    stack_ob = []
    for c in s:
        if is_open_bracket(c):
            stack_ob.append(c)
        elif is_close_bracket(c):
            if get_top(stack_ob) == get_open_bracket(c):
                stack_ob.pop()
            else:
                return False
    return len(stack_ob) == 0
