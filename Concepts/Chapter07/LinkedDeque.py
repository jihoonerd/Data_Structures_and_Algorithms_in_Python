# -*- coding: utf-8 -*-

from Concepts.Chapter07.DoublyLinkedList import _DoublyLinkedBase, Empty


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._header._next._elment

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._trailer