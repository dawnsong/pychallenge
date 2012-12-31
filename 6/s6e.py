#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2012 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import zipfile,re
idx="90052"
file = zipfile.ZipFile("channel.zip", "r")
history = []
while True:
  history.append(idx)
  data = file.read(idx+".txt")
  print "File",idx+":\t"+ data
  idx="".join(re.findall('[0-9.]',data))
  if len(idx)==1:
    break
#Collect the comments
print ''.join([file.getinfo(i+'.txt').comment for i in history])
