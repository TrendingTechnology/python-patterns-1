# -*- coding: utf-8 -*-
# ********************************************************
# Author and developer: Aleksandr Suvorov
# --------------------------------------------------------
# Licensed: BSD 3-Clause License (see LICENSE for details)
# --------------------------------------------------------
# Url: https://github.com/smartlegion/
# --------------------------------------------------------
# Donate: https://smartlegion.github.io/donate
# --------------------------------------------------------
# Copyright © 2021 Aleksandr Suvorov
# ========================================================
# Composite - a pattern that structures objects.
# Arranges objects into tree structures to
# represent part-to-whole hierarchies.
# Allows clients to treat individual and composite
# objects in a consistent manner.
"""Composite"""
from abc import ABC


class Graphic(ABC):

    def draw(self):
        raise NotImplementedError

    def add(self, obj):
        raise NotImplementedError

    def remove(self, obj):
        raise NotImplementedError

    def get_child(self, index):
        raise NotImplementedError


class Line(Graphic, ABC):
    def draw(self):
        print('Line')


class Rectangle(Graphic, ABC):
    def draw(self):
        print('Rectangle')


class Text(Graphic, ABC):
    def draw(self):
        print('Text')


class Picture(Graphic):
    def __init__(self):
        self._children = []

    def add(self, obj):
        if isinstance(obj, Graphic) and obj not in self._children:
            self._children.append(obj)
        else:
            raise TypeError

    def remove(self, obj):
        if obj in self._children:
            index = self._children.index(obj)
            del self._children[index]

    def draw(self):
        for obj in self._children:
            obj.draw()

    def get_child(self, index):
        return self._children[index]


def main():
    pic = Picture()
    pic.add(Line())
    pic.add(Rectangle())
    pic.add(Text())
    pic.draw()
    child = pic.get_child(0)
    print(isinstance(child, Line))  # True
    # Output:
    # -------
    # Line
    # Rectangle
    # Text
    # True


if __name__ == '__main__':
    main()
