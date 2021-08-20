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

from patterns.structural.adapter import Dog


class TestDog:
    def test_dog(self, dog):
        assert isinstance(dog, Dog)

    def test_bark(self, dog):
        assert dog.bark() == 'Brave: wof! wof!'


class TestAdapter:
    def test_cat_adapter(self, dog, cat_adapter):
        dog = cat_adapter('Brave')
        assert dog.bark() == 'Brave: meow! meow!'
