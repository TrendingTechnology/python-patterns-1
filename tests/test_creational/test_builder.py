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
"""Tests builder.py"""


class TestFlashLight:

    def test_on(self, flashlight):
        flashlight.on()
        assert flashlight._shine
        assert 'On' in str(flashlight)

    def test_off(self, flashlight):
        flashlight.off()
        assert not flashlight._shine
        assert 'Off' in str(flashlight)


class TestFlashLightBuilder:
    def test_build_body(self, flashlight_builder, body):
        assert isinstance(flashlight_builder.build_body(), type(body))

    def test_build_lamp(self, flashlight_builder, lamp):
        assert isinstance(flashlight_builder.build_lamp(), type(lamp))

    def test_build_battery(self, flashlight_builder, battery):
        assert isinstance(flashlight_builder.build_battery(), type(battery))

    def test_create_flashlight(self, flashlight_builder, flashlight):
        assert isinstance(flashlight_builder.create_flashlight(), type(flashlight))
