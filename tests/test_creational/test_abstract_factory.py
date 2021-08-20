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
"""Test abstract_factory.py"""
import pytest

from patterns.creational.abstract_factory import ConcreteFactory1, ConcreteFactory2


class TestDrink:
    def test_name(self, drink_obj):
        assert drink_obj.name == 'Coca Cola'


class TestFood:
    def test_name(self, food_obj):
        assert food_obj.name == 'Nuts'


class TestConcreteFactory1:
    def test_create_drink(self, fac1, drink):
        assert isinstance(fac1.create_drink(), drink)

    def test_create_food(self, fac2, food):
        assert isinstance(fac2.create_food(), food)


@pytest.mark.parametrize('n, obj', [(0, ConcreteFactory1), (1, ConcreteFactory2)])
def test_get_factory(n, obj, get_factory):
    assert isinstance(get_factory(n), obj)
