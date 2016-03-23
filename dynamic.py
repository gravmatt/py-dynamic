# -*- coding: utf-8 -*-
"""
Copyright (c) 2016, René Tanczos <gravmatt@gmail.com> (Twitter @gravmatt)
The MIT License (MIT)

Class to create dynamic objects.

Project on github https://github.com/gravmatt/py-dynamic
"""

__author__ = 'Rene Tanczos'
__version__ = '0.1'
__license__ = 'MIT'

class Dynamic:
    def __init__(self, strict=True):
        self.__dict__['__strict'] = strict
        self.me = 'rene'


    def __getattr__(self, name):
        if(name in self.__dict__):
            return self.__dict__[name]
        else:
            if(self.__dict__['__strict']):
                raise AttributeError('Property \'%s\' not found' % name)
            else:
                return None


    def __setattr__(self, name, value):
        self.__dict__[name] = value


    def __delattr__(self, name):
        if(name in self.__dict__):
            del self.__dict__[name]
        else:
            if(self.__dict__['__strict']):
                raise AttributeError('Property \'%s\' not found' % name)
