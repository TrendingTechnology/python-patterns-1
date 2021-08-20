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


class WindowBase:
    def show(self):
        raise NotImplementedError()

    def hide(self):
        raise NotImplementedError()


class MainWindow(WindowBase):
    def show(self):
        print('Show MainWindow')

    def hide(self):
        print('Hide MainWindow')


class SettingWindow(WindowBase):
    def show(self):
        print('Show SettingWindow')

    def hide(self):
        print('Hide SettingWindow')


class HelpWindow(WindowBase):
    def show(self):
        print('Show HelpWindow')

    def hide(self):
        print('Hide HelpWindow')


class WindowMediator:
    def __init__(self):
        self.windows = dict.fromkeys(['main', 'setting', 'help'])

    def show(self, win):
        for window in self.windows.values():
            if window is not win:
                window.hide()
        win.show()

    def set_main(self, win):
        self.windows['main'] = win

    def set_setting(self, win):
        self.windows['setting'] = win

    def set_help(self, win):
        self.windows['help'] = win


if __name__ == '__main__':
    main_win = MainWindow()
    setting_win = SettingWindow()
    help_win = HelpWindow()

    med = WindowMediator()
    med.set_main(main_win)
    med.set_setting(setting_win)
    med.set_help(help_win)

    main_win.show()
    # Show MainWindow

    med.show(setting_win)
    # Hide MainWindow
    # Hide HelpWindow
    # Show SettingWindow

    med.show(help_win)
    # Hide MainWindow
    # Hide SettingWindow
    # Show HelpWindow
