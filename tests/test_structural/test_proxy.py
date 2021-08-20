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


class TestImageProxy:
    def test_draw(self, image_proxy, capfd):
        image_proxy.draw(0, 0, 'green')
        image_proxy.draw(0, 1, 'green')
        assert len(image_proxy.operations) == 2

    def test_fill(self, image_proxy):
        image_proxy.fill('gray')
        assert len(image_proxy.operations) == 1

    def test_save(self, image_proxy, capfd):
        image_proxy.fill('gray')
        image_proxy.draw(0, 0, 'green')
        image_proxy.draw(0, 1, 'green')
        image_proxy.draw(1, 0, 'green')
        image_proxy.draw(1, 1, 'green')
        image_proxy.save('image.png')
        out, _ = capfd.readouterr()
        assert 'Saves the image to a file: image.png\n' in out
