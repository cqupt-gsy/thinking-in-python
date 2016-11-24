__author__ = 'Mentu'

from distutils.core import setup, Extension

setup (name = 'mypackge',
       version = '1.0',
       description = 'Caldistance module',
       ext_modules = [Extension('caldistance',['CalDistance.c','CalDistance.i'])
       ]
)