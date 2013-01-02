#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2012 Xiao-Wei Song <dawnwei.song@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import sys 
from PIL import Image
img=Image.open('oxygen7.png')
for i in range(3,611,7): sys.stdout.write(chr( img.getpixel((i,4))[0] ))
msg= ''.join(chr( img.getpixel((i,4))[0] )  for i in range(3,611,7) )
import re
n=re.findall('\[.*\]', msg)[0]
import ast
c=ast.literal_eval(n)
print 'result: '
print ''.join(chr(x) for x in c)
sys.exit()
