#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2012 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

hint=open('hint','r').read()
import re 
x=re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]',hint)
print ''.join(x)
