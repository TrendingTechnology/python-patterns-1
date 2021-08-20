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


class Subject:
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):
        # subscribe to the alert
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        # unsubscribe from notification
        self._observers.remove(observer)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        # notify all observers about the event
        for observer in self._observers:
            observer.update(data)


class ObserverBase:
    """Abstract observer"""
    def update(self, data):
        raise NotImplementedError()


class Observer(ObserverBase):
    """Observer"""
    def __init__(self, name):
        self._name = name

    def update(self, data):
        print(f'{self._name}: {data}')


if __name__ == '__main__':
    subject = Subject()
    subject.attach(Observer('Observer 1 '))
    subject.attach(Observer('Observer 2'))
    subject.set_data('observer data')

    # # Output:
    #
    # Observer 1 : observer data
    # Observer 2: observer data
