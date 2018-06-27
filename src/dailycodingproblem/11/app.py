"""
https://en.wikipedia.org/wiki/Trie

"""
from collections import defaultdict
from itertools import chain
from queue import Queue
from typing import Any, Iterable, Iterator, Optional


class Trie:
    def __init__(self, letter=None):
        self.m_children = defaultdict(lambda: None)
        if letter:
            self.m_children[letter] = None

    def get_node(self, l: Any) -> Optional[Iterable]:
        """
        Return node from character.
        If character exist, return trie node associated
        else return None (is a leaf child)

        :param l:
        :return:
        """
        return self.m_children[l]

    def add_word(self, w: Iterable):
        """
        Add a word from the root

        :param w:
        :return:
        """
        cur_node = self
        for l in w:
            next_node = cur_node.get_node(l)
            if next_node is None:
                next_node = Trie()
                cur_node.m_children[l] = next_node
            cur_node = next_node

    def get_words(self) -> Iterator[Iterable]:
        """
        Return all words from the root to all leaf children
        :return:
        """
        q_childs = Queue()
        for l, childs in self.m_children.items():
            q_childs.put((l, childs))

        while not q_childs.empty():
            word, cur_node = q_childs.get()
            if bool(cur_node.m_children):
                for l, childs in cur_node.m_children.items():
                    q_childs.put((word + l, childs))
            else:
                yield word

    def find_prefix(self, prefix: Iterable) -> 'Trie':
        """
        Try to return Trie Node from prefix traverse

        :param prefix:
        :return:
        """
        cur_node = self
        for l in prefix:
            next_node = cur_node.get_node(l)
            if next_node is None:
                return cur_node
            cur_node = next_node
        return cur_node

    def find_elements_with_prefix(self, prefix: Iterable) -> Optional[Iterable]:
        """

        :param prefix:
        :return:
        """
        t_prefix = self.find_prefix(prefix)
        if t_prefix:
            for w in t_prefix.get_words():
                yield chain(prefix, w)
        else:
            return None


if __name__ == '__main__':
    def test():
        t = Trie()
        t.add_word('dog')
        t.add_word('deer')
        t.add_word('deal')
        t_prefix = t.find_prefix('de')
        print(list(t.get_words()))
        print(list(t_prefix.get_words()))
        print(["".join(w) for w in t.find_elements_with_prefix('de')])

    test()
