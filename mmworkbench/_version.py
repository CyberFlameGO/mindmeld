# -*- coding: utf-8 -*-
"""Defines mmworkbench version information"""
from __future__ import absolute_import, unicode_literals

current = '4.0.0post11'


def _get_wb_version():
    import mmworkbench as wb
    return wb.__version__
