# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: t_getopt.py 
@time: 2018/03/19 
"""
import sys
from getopt import getopt

city = ''
tax_config_file = ''
user_data_file = ''
salary_file = ''
try:
    opts, args = getopt(sys.argv[1:], 'C:c:d:o:')
    for opt, arg in opts:
        if opt in ('-C'):
            city = arg
        if opt in ('-c'):
            tax_config_file = arg
        if opt == '-d':
            user_data_file = arg
        if opt == '-o':
            salary_file = arg
except getopt.GetoptError:
    print('parameter error')
    exit(-1)







