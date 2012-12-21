#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2012 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import urllib

base='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
n=0;
n+=1;
f=urllib.urlopen(base % '12345')
while n<=400:
  n=n+1;
  x=f.read();
  print x.split()[-1];
  f=urllib.urlopen(base % x.split()[-1])
