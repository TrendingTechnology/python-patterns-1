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
"""Tests factory.py"""
import pytest

from patterns.creational.factory import PDFDocument, ODFDocument, NoneDocument


class TestApplication:
    @pytest.mark.parametrize('type_, obj', [('pdf', PDFDocument),
                                            ('odf', ODFDocument),
                                            ('bad', NoneDocument)])
    def test_create_doc(self, obj, app, type_):
        assert isinstance(app.create_doc(type_), obj)
