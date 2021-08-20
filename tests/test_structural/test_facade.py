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


class TestFacade:
    def test_write(self, facade, capfd):
        facade.write('Smart Legion')
        out, err = capfd.readouterr()
        assert out == 'Smart Legion\n'

    def test_write_err(self, facade, capfd):
        facade.write('Smart Legion')
        out, err = capfd.readouterr()
        assert out == 'Error: paper out\n'
