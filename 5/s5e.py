#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2012 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""
http://unixwars.com/2007/09/11/python-challenge-level-5-peak-hell/
"""
import urllib,pickle
url='http://www.pythonchallenge.com/pc/def/banner.p'
obj=pickle.load(urllib.urlopen(url))
for line in obj:
      print ''.join(map(lambda pair: pair[0]*pair[1], line))
