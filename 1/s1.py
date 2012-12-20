#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2012 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import string 

ftab=string.ascii_lowercase;
ttab=ftab[2:]+ftab[0:2];
tt=string.maketrans(ftab, ttab);
hint=open('hint','r').read();
print hint.translate(tt)
print 'map'.translate(tt)
