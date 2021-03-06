#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:25:49 2018

@author: niels-peter
"""

from xbrl_ai import xbrlinstance_to_dict, xbrldict_to_xbrl_54

__title__ = 'test_xbrl_ai_us'
__version__ = '0.0.2'
__author__ = 'Niels-Peter Rønmos'

file = open('goog-20151231.xml', 'r')
file_indhold = file.read()

xbrl = xbrlinstance_to_dict(file_indhold)
xbrl_as_54 = xbrldict_to_xbrl_54(xbrl)
