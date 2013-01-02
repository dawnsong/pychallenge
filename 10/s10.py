#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""
https://en.wikipedia.org/wiki/Look-and-say_sequence
look and say
http://docs.python.org/2/library/itertools.html#itertools.groupby

"""

import itertools
def next_morris(number):
    return ''.join('%s%s' % (len(list(group)), digit)
                   for digit, group in itertools.groupby(str(number)))
x  =next_morris(1)
for i in range(2,31):
  x=next_morris(x)
  print len(x)
