#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 20:32:03 2019

@author: pete
"""

import glob
path=glob.glob('*/')
#folders = [f for f in glob.glob(path + "**/", recursive=True)]
folders = [f for f in glob.glob(path , recursive=True)]
for f in folders:
    print(f)

import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    # do something