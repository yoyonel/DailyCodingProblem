"""
This problem was asked by Google.
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
"""
import attr
from itertools import tee
from typing import Any, Iterator, Optional


@attr.s
class Node:
    value: Any = attr.ib()
    next: Optional['Node'] = attr.ib(default=None)

    def set_next(self, node: 'Node'):
        self.next = node


@attr.s
class LinkedList:
    root: Optional['Node'] = attr.ib(default=None)

    @classmethod
    def from_nodes(cls, nodes: Iterator['Node']):
        n0, n1 = tee(nodes)
        root = next(n1)
        for cur_node, next_node in zip(n0, n1):
            cur_node.set_next(next_node)
        return cls(root)

    def find_intersecting_node(self, other: 'LinkedList'):
        # make linked list `a` cyclic (and count the number of nodes)
        # searching last node
        cur_node = self.root
        i = 1
        while cur_node.next is not None:
            cur_node = cur_node.next
            i += 1
        # make the cycle
        cur_node.next = self.root
        last_node = cur_node

        #
        offset_cycle_node = other.root
        for _ in range(i):
            offset_cycle_node = offset_cycle_node.next

        cur_node = other.root
        while offset_cycle_node != cur_node:
            cur_node = cur_node.next
            offset_cycle_node = offset_cycle_node.next

        # undo cycle
        last_node.next = None

        return cur_node


def main():
    intersecting_node = Node(8)

    a = LinkedList.from_nodes(
        [
            Node(3),
            Node(7),
            intersecting_node,
            Node(10)
        ]
    )
    b = LinkedList.from_nodes(
        [
            Node(99),
            Node(1),
            intersecting_node,
        ]
    )

    print(f'a={a}')
    print(f'b={b}')

    # # make linked list `a` cyclic (and count the number of nodes)
    # a_root = a.root
    # a_cur_node = a_root
    # i = 1
    # while a_cur_node.next is not None:
    #     a_cur_node = a_cur_node.next
    #     i += 1
    # a_cur_node.next = a_root
    # print(f'|a|={i}')
    #
    # #
    # b_next_cycle = b.root.next
    # for _ in range(i-1):
    #     b_next_cycle = b_next_cycle.next
    # # print(b_next_cycle.value)
    #
    # b_cur = b.root
    # while b_next_cycle != b_cur:
    #     b_cur = b_cur.next
    #     b_next_cycle = b_next_cycle.next
    # assert id(b_cur) == id(b_cur)
    print(a.find_intersecting_node(b))


if __name__ == '__main__':
    main()
