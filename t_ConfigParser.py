# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Administrator
@file: t_ConfigParser.py
@time: 2018/03/19
"""
import configparser

config = configparser.RawConfigParser()
config.read('test.cfg')
JiShuL = config.getfloat('DEFAULT','JiShuL')
JiShuH = config.getfloat('DEFAULT','JiShuH')
YangLao = config.getfloat('DEFAULT','YangLao')
YiLiao = config.getfloat('DEFAULT','YiLiao')
ShiYe = config.getfloat('DEFAULT','ShiYe')
GongShang = config.getfloat('DEFAULT','GongShang')
ShengYu = config.getfloat('DEFAULT','ShengYu')
GongJiJin = config.getfloat('DEFAULT','GongJiJin')

