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
# Facade - a pattern that structures objects.
# Provides a unified interface instead of a set
# of interfaces for some subsystem.
# The facade defines a higher-level interface that
# makes the subsystem easier to use.
"""Facade"""


class Paper:
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def draw(self, text):
        if self.get_count() > 0:
            self._count -= 1
            print(text)


class Printer:
    @staticmethod
    def error(msg):
        print(f'Error: {msg}')

    def print_(self, paper, text):
        if paper.get_count() > 0:
            paper.draw(text)
        else:
            self.error('paper out')


class Facade:
    def __init__(self):
        self._printer = Printer()
        self._paper = Paper(1)

    def write(self, text):
        self._printer.print_(self._paper, text)


def main():
    f = Facade()
    f.write('Hello world!')  # Hello world!
    f.write('Hello world!')  # Error: paper out


if __name__ == '__main__':
    main()
