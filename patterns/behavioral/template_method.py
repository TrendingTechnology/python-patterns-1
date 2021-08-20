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


class ExampleBase:
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    def step_one(self):
        raise NotImplementedError()

    def step_two(self):
        raise NotImplementedError()

    def step_three(self):
        raise NotImplementedError()


class Example(ExampleBase):
    def step_one(self):
        print('The first step of the algorithm')

    def step_two(self):
        print('The second step of the algorithm')

    def step_three(self):
        print('The third step of the algorithm')


if __name__ == '__main__':
    example = Example()
    example.template_method()
    # The first step of the algorithm
    # The second step of the algorithm
    # The third step of the algorithm
