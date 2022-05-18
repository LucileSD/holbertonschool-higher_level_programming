#!/usr/bin/python3
"""Node class file"""


class Node:
    """
    class node defines a node of a single linked list
    """

    def __init__(self, data, next_node=None):
        """
        Init a node
        Return: None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        data getter
        Return: self.__data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data setter
        args:
            value: value in the node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        next_node getter
        Return: self.__next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next_node setter
        args:
            value: value in the node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList defines a singly linked list
    """

    def __init__(self):
        """
        Init a linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        insert a new node at the correct position
        args:
            value: value to insert in the node
        """
        tmp = self.__head
        new = Node(value)
        if not self.__head or value < self.__head.data:
            if self.__head:
                new.next_node = self.__head
            self.__head = new
        else:
            while (tmp.next_node):
                if tmp.next_node.data >= value:
                    break
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """
        Print the linked list
        Return: String to print
        """
        string = ""
        tmp = self.__head
        while (tmp):
            string += str(tmp.data)
            if (tmp.next_node):
                string += '\n'
            tmp = tmp.next_node
        return string
