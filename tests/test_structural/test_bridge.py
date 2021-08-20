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


class TestRemoteControl:
    def test_channel(self, remote_control):
        assert remote_control._channel == 0

    def test_tune_channel(self, remote_control):
        remote_control.tune_channel(10)
        assert remote_control._channel == 10

    def test_next_channel(self, remote_control):
        remote_control.next_channel()
        assert remote_control._channel == 1

    def test_prev_channel(self, remote_control):
        remote_control.tune_channel(10)
        remote_control.prev_channel()
        assert remote_control._channel == 9
