# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:30:38 2018

@author: Brandon
"""

import os
def(s):
    try:
        x=int(s)
    except (ValueError,TypeError) as e:#this is assignment
        print("conversion eror:{}".format(str(e)),,