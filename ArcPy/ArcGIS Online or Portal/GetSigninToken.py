# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 12:58:02 2022

@author: Reza
"""


import arcpy

token = arcpy.GetSigninToken()
if token is not None:
    print(token['token'])