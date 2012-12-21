#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2012 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import pickle,sys
hint=pickle.load(open('hint','r'))
for y in hint:
  for yy in y:
    sys.stdout.write(yy[0]*yy[1])
  sys.stdout.write('\n')  
