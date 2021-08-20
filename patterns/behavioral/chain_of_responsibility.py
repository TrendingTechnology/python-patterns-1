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


class HttpHandler:
    def handle(self, code):
        raise NotImplementedError()


class Http404Handler(HttpHandler):
    def handle(self, code):
        if code == 404:
            return 'Page not found'


class Http500Handler(HttpHandler):
    def handle(self, code):
        if code == 500:
            return 'server error'


class Client:
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print('Answer: %s' % msg)
                break
        else:
            print('Code not processed')


if __name__ == '__main__':
    client = Client()
    client.add_handler(Http404Handler())
    client.add_handler(Http500Handler())
    client.response(400)
    client.response(404)
    client.response(500)

    # Output:

    # Code not processed
    # Answer: Page not found
    # Answer: Server error
