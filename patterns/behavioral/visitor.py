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


class FruitVisitor:
    """Visitor"""
    def draw(self, fruit):
        methods = {
            Apple: self.draw_apple,
            Pear: self.draw_pear,
        }
        draw = methods.get(type(fruit), self.draw_unknown)
        draw(fruit)

    def draw_apple(self, fruit):
        print('Apple')
        return fruit

    def draw_pear(self, fruit):
        print('Pear')
        return fruit

    def draw_unknown(self, fruit):
        print('Fruit')
        return fruit


class Fruit:
    """Fruits"""
    def draw(self, visitor_):
        visitor_.draw(self)


class Apple(Fruit):
    """Apple"""


class Pear(Fruit):
    """Pear"""


class Banana(Fruit):
    """Banana"""


if __name__ == '__main__':
    visitor = FruitVisitor()

    apple = Apple()
    apple.draw(visitor)
    # Apple

    pear = Pear()
    pear.draw(visitor)
    # Pear

    banana = Banana()
    banana.draw(visitor)
    # Fruit

