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
"""Tests prototype.py"""
from patterns.creational.prototype import Bird


class TestPrototype:
    def test_register(self, prototype, bird):
        prototype.register('Bird', bird)
        assert 'Bird' in prototype._objects

    def test_unregister(self, prototype, bird):
        prototype.register('Bird', bird)
        prototype.unregister('Bird')
        assert 'Bird' not in prototype._objects

    def test_clone(self, prototype, bird):
        prototype.register('Bird', bird)
        duck = prototype.clone('Bird', {'name': 'Duck'})
        assert isinstance(duck, Bird)

    def test_get_attr(self, prototype, bird):
        prototype.register('Bird', bird)
        duck = prototype.clone('Bird', {'name': 'Duck'})
        assert getattr(duck, 'name')
        assert duck.name == 'Duck'
