"""

"""
import attr
import math
from queue import Queue
from typing import Any, Optional


@attr.s
class UnivalTree:
    value: Any = attr.ib()
    left: Optional['UnivalTree'] = attr.ib(default=None)
    right: Optional['UnivalTree'] = attr.ib(default=None)

    def is_leaf(self):
        return self.left is None and self.right is None

    def count_unival_subtrees_2(self):
        q_nodes = Queue()

        def _eval_branch_node(root_node, root_count, branch_node) -> int:
            count_ust_from_branch = 0
            if branch_node:
                continue_values = branch_node.value == root_node.value
                if not continue_values:
                    count_ust_from_branch = math.factorial(root_count) if root_count > 0 else 0
                q_nodes.put([branch_node, root_count + 1 if continue_values else 0])
            return count_ust_from_branch

        count_ust = 0
        q_nodes.put([self, 0])
        while not q_nodes.empty():
            root_node, count = q_nodes.get()
            # Is leaf ?
            if root_node.is_leaf():
                count_ust += math.factorial(count) if count > 0 else 0
            else:
                # eval left branch
                count_ust += _eval_branch_node(root_node, count, root_node.left)
                # eval right branch
                count_ust += _eval_branch_node(root_node, count, root_node.right)
        return count_ust

    def count_unival_subtrees(self):
        count, _ = self.helper(self)
        return count

    # Also returns number of unival subtrees, and whether it is itself a unival subtree.
    @staticmethod
    def helper(root):
        # end of recursion
        if root is None:
            return 0, True

        # recursion step
        # on left
        left_count, is_left_unival = root.helper(root.left)
        # on right
        right_count, is_right_unival = root.helper(root.right)
        # sum the count for each branches
        total_count = left_count + right_count
        # this root is a root of unit subtree ?
        # first: leaves branches are univals ?
        if is_left_unival and is_right_unival:
            # value associate to left branch is the same of root value ?
            if root.left is not None and root.value != root.left.value:
                # not unival
                return total_count, False
            # value associate to right branch is the same of root value ?
            if root.right is not None and root.value != root.right.value:
                # not unival
                return total_count, False
            # up the sum of unival subtree => root is one
            return total_count + 1, True
        # not unival
        return total_count, False


def main():
    """
           0
         /  \
        0    0
            / \
           1   0
          / \
         1  1
        """
    ut = UnivalTree(
        0,
        UnivalTree(1),
        UnivalTree(
            0,
            UnivalTree(
                1,
                UnivalTree(1),
                UnivalTree(1)
            ),
            UnivalTree(0)
        )
    )
    assert ut.count_unival_subtrees() == 5

    """
      a
     / \
    a   a
        /\
       a  a
           \
            A
    """
    ut = UnivalTree(
        'a',
        UnivalTree('a'),
        UnivalTree(
            'a',
            UnivalTree('a'),
            UnivalTree(
                'a',
                None,
                UnivalTree('A')
            )
        )
    )
    assert ut.count_unival_subtrees() == 3

    """
      a
     / \
    c   b
        /\
       b  b
           \
            b
    """
    ut = UnivalTree(
        'a',
        UnivalTree('c'),
        UnivalTree(
            'b',
            UnivalTree('b'),
            UnivalTree(
                'b',
                None,
                UnivalTree('b')
            )
        )
    )
    assert ut.count_unival_subtrees() == 5

    """
       1
     /  \
    1    1
        / \
       1   1
      / \
     1   1
    """
    ut = UnivalTree(
        1,
        UnivalTree(1),
        UnivalTree(
            1,
            UnivalTree(
                1,
                UnivalTree(1),
                UnivalTree(1)
            ),
            UnivalTree(1)
        )
    )
    assert ut.count_unival_subtrees() == 7


if __name__ == '__main__':
    main()
