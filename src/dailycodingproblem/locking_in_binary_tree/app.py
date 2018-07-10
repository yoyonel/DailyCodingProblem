"""

"""
from binarytree import Node, NodeTypeError
from dailycodingproblem.locking_in_binary_tree.overload_binarytree import build


class NodeWithLock(Node):
    def __init__(self, *args, **kwargs):
        if 'parent' in kwargs and not isinstance(kwargs['parent'], Node):
            raise NodeTypeError('parent must be a Node instance')
        super().__init__(*args, **kwargs)

        self.parent = kwargs.get('parent', None)

        self.isLocked = False
        self.nbDescendantsLocked = 0

    @property
    def is_locked(self):
        return self.isLocked

    def is_state_can_be_changed(self) -> bool:
        """
        -> O(h)

        :return:
        """
        # All descendants are unlock ?
        if self.nbDescendantsLocked == 0:
            return True
        # All ancestors are unlock ?
        node = self.parent  # type: 'NodeWithLock'
        while node is not None:
            if node.is_locked:
                break
            # next parent
            node = node.parent
        return node is None

    def change_state_lock(self, newStateLock: bool) -> bool:
        """
        -> 2 * O(h) ~ O(h)

        :param newStateLock:
        :return:
        """
        if self.is_state_can_be_changed():  # O(h)
            self.isLocked = newStateLock
            # Update all ancestors: a new descendant is lock
            node = self.parent
            incr = 1 if newStateLock else -1
            # O(h)
            while node is not None: # no more parent ? (root node)
                # update the number of descendants locked for this node/ancestor
                node.nbDescendantsLocked += incr
                # next parent
                node = node.parent
            return True
        else:
            return False

    def lock(self):
        """
        Attempts to lock the node.

        Return True if it can be locked
        Return False if it cannot be locked
        :return:
        """
        return self.change_state_lock(True)

    def unlock(self):
        """
        Unlocks the node.

        Return True if it can be unlocked
        Return False if it cannot be unlocked
        :return:
        """
        return self.change_state_lock(False)


def main():
    """
               _____________U-0_____________
              /                             \
           _U-0_____                   _____U-0_
          /         \                 /         \
        U-0        _U-0_           _U-0_        U-0
                  /     \         /     \
                U-0     U-0     U-0     U-0

        Node index=0, value=1 ->
            try to 'Lock' the node - result: True
        Node index=9, value=2 ->
            try to 'Lock' the node - result: True
        Node index=3, value=8 ->
            try to 'Lock' the node - result: True
        Node index=4, value=14 ->
            try to 'Lock' the node - result: False
        Node index=1, value=13 ->
            try to 'Lock' the node - result: False
        Node index=1, value=13 ->
            try to 'Unlock' the node - result: False

               _____________L-2_____________
              /                             \
           _U-2_____                   _____U-0_
          /         \                 /         \
        L-0        _U-1_           _U-0_        U-0
                  /     \         /     \
                L-0     U-0     U-0     U-0

        Node index=9, value=2 ->
            try to 'Unlock' the node - result: True
        Node index=1, value=13 ->
            try to 'Lock' the node - result: False
        Node index=4, value=14 ->
            try to 'Lock' the node - result: True
        Node index=2, value=10 ->
            try to 'Lock' the node - result: True

               _____________L-3_____________
              /                             \
           _U-2_____                   _____L-0_
          /         \                 /         \
        L-0        _L-0_           _U-0_        U-0
                  /     \         /     \
                U-0     U-0     U-0     U-0

    :return:
    """
    mytree = build([1, 13, 10, 8, 14, 11, 0, None, None, 2, 7, 9, 6], TNode=NodeWithLock)
    mytree.pprint(index=True)

    for index_node, lock_the_node in [
        (0, True),
        (9, True),
        (3, True),
        (4, True),
        (1, True),
        (1, False),
    ]:
        print(f"Node index={index_node}, value={mytree[index_node].value} -> ")
        if lock_the_node:
            print(f"\ttry to 'Lock' the node - result: {mytree[index_node].lock()}")
        else:
            print(f"\ttry to 'Unlock' the node - result: {mytree[index_node].unlock()}")
    mytree.pprint(index=True)

    for index_node, lock_the_node in [
        (9, False),
        (1, True),
        (4, True),
        (2, True),
    ]:
        print(f"Node index={index_node}, value={mytree[index_node].value} -> ")
        if lock_the_node:
            print(f"\ttry to 'Lock' the node - result: {mytree[index_node].lock()}")
        else:
            print(f"\ttry to 'Unlock' the node - result: {mytree[index_node].unlock()}")
    mytree.pprint(index=True)


if __name__ == '__main__':
    main()
