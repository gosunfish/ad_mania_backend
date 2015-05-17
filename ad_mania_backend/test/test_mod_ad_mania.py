#!/usr/bin/env python

"""
test code for ad_mania module

can be run with py.test or nosetests
"""

def test_init():
    """ makes sure it imports and can be read"""
    import run
    assert hasattr(run, '__version__')

