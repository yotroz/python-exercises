#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:36:04 2018

@author: yotroz
"""

def linear(lst, num): 
    for i in range(len(lst)): 
        
        if lst[i] == num: 
            return i
        
    return None     
#%%

def hello(): 
    name = input("What's you name?")
    print("hello " + name)    