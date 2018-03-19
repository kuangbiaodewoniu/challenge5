# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Administrator
@file: get_city.py
@time: 2018/03/19
"""
from  getopt import  getopt
import sys
def get_city():
    opts, args = getopt(sys.argv[1:], 'C')
    return args[0].upper()
