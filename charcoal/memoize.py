# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t; python-indent: 4 -*-


def memoize(function):
    return Memoize(function)


class Memoize(object):
    def __init__(self, fn):
        self.cache = {}
        self.fn = fn

    def __get__(self, instance, cls=None):
        self.instance = instance
        return self

    def __call__(self,*args):
        if self.cache.has_key(args):
            return self.cache[args]
        else:
            object = self.cache[args] = self.fn(self.instance, *args)
            return object