#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""
http://unixwars.com/2007/09/18/python-challenge-level-12-dealing-evil/
"""

info=open("evil2.gfx").read()
[open("12_f%d.dat" %i, "w").write(info[i::5]) for i in range(5)]
