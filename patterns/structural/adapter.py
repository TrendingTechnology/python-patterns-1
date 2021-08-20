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
# An adapter is a pattern that structures
# classes and objects.
# Converts the interface of one class to the interface
# of another that clients expect.
# The adapter allows classes with incompatible interfaces
# to work together that would not be possible without it.
"""Adapter"""


class Dog:
    def __init__(self, name):
        self._name = name

    def bark(self):
        return f'{self._name}: wof! wof!'

    @property
    def name(self):
        return self._name


class Cat:
    def __init__(self, name):
        self._name = name

    def meow(self):
        return f'{self._name}: meow! meow!'

    @property
    def name(self):
        return self._name


class CatAdapter(Dog):
    def __init__(self, name):
        super(CatAdapter, self).__init__(name=name)
        self._cat = Cat(name=name)

    def bark(self):
        # We use the interface of the `Dog` class,
        # and the implementation of the` Cat` class.
        return self._cat.meow()


def main():
    # Dog object
    dog = Dog('Brave')
    print(dog.bark())  # Brave wof! wof!

    # We create a customized object.
    # We use the interface of the `Dog` class,
    # and the implementation of the` Cat` class.
    dog_adapted = CatAdapter('Brave')
    print(dog_adapted.bark())  # Brave meow! meow!


if __name__ == '__main__':
    main()
