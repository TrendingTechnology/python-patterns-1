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


class RomanNumeralInterpreter:
    """Roman numeral interpreter"""
    def __init__(self):
        self.grammar = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def interpret(self, text):
        numbers = list(map(self.grammar.get, text))  # строки в значения
        if None in numbers:
            raise ValueError('Wrong value: %s' % text)
        result = 0
        temp = None
        while numbers:
            num = numbers.pop(0)
            if temp is None or temp >= num:
                result += num
            else:
                result += (num - temp * 2)
            temp = num
        return result


if __name__ == '__main__':
    interp = RomanNumeralInterpreter()
    print(interp.interpret('MMMCMXCIX') == 3999)  # True
    print(interp.interpret('MCMLXXXVIII') == 1988)  # True

