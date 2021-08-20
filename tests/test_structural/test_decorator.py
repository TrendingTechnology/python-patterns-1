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


class TestDecorator:
    def test_fly(self, man_jet, capfd):
        man_jet.fly()
        out, err = capfd.readouterr()
        assert out == 'Smart Bear flies on a jetpack.\n'


def test_man(man, capfd):
    man.say()
    out, err = capfd.readouterr()
    assert out == 'Hello, my name is Smart Bear.\n'
