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
# Bridge - a pattern that structures objects.
# The main task is to separate the abstraction
# from its implementation so that
# so that both can be changed independently.
"""Bridge"""
from abc import ABC, abstractmethod


class TvBase(ABC):
    @abstractmethod
    def tune_channel(self, channel):
        pass


class SharpTv(TvBase):
    def tune_channel(self, channel):
        print(f'{self.__class__.__name__}: selected {channel} channel.')


class SonyTv(TvBase):
    def tune_channel(self, channel):
        print(f'SonyTv: selected {channel} channel.')


class RemoteControlBase(ABC):
    def __init__(self):
        self._tv = self.get_tv()

    @abstractmethod
    def get_tv(self):
        pass

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    def __init__(self):
        super(RemoteControl, self).__init__()
        self._channel = 0

    def get_tv(self):
        return SharpTv()

    def tune_channel(self, channel):
        super(RemoteControl, self).tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def prev_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)

    def reset_channel(self):
        self._channel = 0
        self.tune_channel(self._channel)
    

def main():
    remote_control = RemoteControl()
    remote_control.tune_channel(5)  # SharpTv: selected 5 channel.
    remote_control.prev_channel()  # SharpTv: selected 4 channel.
    remote_control.next_channel()  # SharpTv: selected 5 channel.
    remote_control.reset_channel()  # SharpTv: selected 0 channel.


if __name__ == '__main__':
    main()
