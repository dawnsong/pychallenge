#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2012 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import string,sys
hint=open('hint','r').read()
for x in hint:
  if x in string.ascii_letters:
    sys.stdout.write(x)
