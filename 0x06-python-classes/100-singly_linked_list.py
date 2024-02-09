#!/usr/bin/python3
"""Define a class for a singly linked list."""

class Node:
    """Respresents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set data of node"""
        return (self.__data)

    @property
    def next_node(self):
        """Get/set data of next node."""
        return (self.__next_node)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance (value, Node) and not isinstance(value, None):
            raise TypeError("next_node must be node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initializes a singly linked list."""

        self.head = None

    def sorted_insert(self, value):
        """Define the print() representation of a SinglyLinkedList."""

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = new
            self.__head = new
        else:
            temp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                temp = temp.next_node
                tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
