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
from abc import ABC


class Light:

    @staticmethod
    def turn_on():
        print('To turn on the light')

    @staticmethod
    def turn_off():
        print('Turn the lights off')


class CommandBase:
    def execute(self):
        raise NotImplementedError()


class LightCommandBase(CommandBase, ABC):
    def __init__(self, light_):
        self.light = light_


class TurnOnLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_off()


class Switch:
    def __init__(self, on_cmd, off_cmd):
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd

    def on(self):
        self.on_cmd.execute()

    def off(self):
        self.off_cmd.execute()


if __name__ == '__main__':
    light = Light()
    switch = Switch(on_cmd=TurnOnLightCommand(light),
                    off_cmd=TurnOffLightCommand(light))
    switch.on()
    switch.off()

    # Output:

    # To turn on the light
    # Turn the lights off

