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


class ImageDecoder:
    @staticmethod
    def decode(filename):
        raise NotImplementedError()


class PNGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('PNG decode')


class JPEGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('JPEG decode')
        return 'JPEG decode'


class GIFImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('GIF decode')
        return 'GIF decode'


class Image:
    @classmethod
    def open(cls, filename):
        ext = filename.rsplit('.', 1)[-1]
        if ext == 'png':
            decoder = PNGImageDecoder
        elif ext in ('jpg', 'jpeg'):
            decoder = JPEGImageDecoder
        elif ext == 'gif':
            decoder = GIFImageDecoder
        else:
            raise RuntimeError('Unable to decode file %s' % filename)
        byte_range = decoder.decode(filename)
        return cls(byte_range, filename)

    def __init__(self, byte_range, filename):
        self._byte_range = byte_range
        self._filename = filename


if __name__ == '__main__':
    Image.open('picture.png')  # PNG decode
    Image.open('picture.jpg')  # JPEG decode
    Image.open('picture.gif')  # GIF decode
