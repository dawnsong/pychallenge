#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2012 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import zipfile
hint=zipfile.ZipFile('channel.zip','r')
print hint.read('readme.txt')
n='90052'
import re
infos=''
while (None is not re.match('[0-9]+',n)):
  msg=hint.read('%s.txt' % n)
  print msg
  info=hint.getinfo('%s.txt' % n)
  infos+=info.comment
  #print info.comment
  n=msg.split()[-1]

print infos
