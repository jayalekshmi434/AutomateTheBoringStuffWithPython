# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:35:33 2021

@author: jayal
"""

# This function takes a list and returns a strinf with the items in the list comma separated
# and add "and" before the last item
def commaCode(myList):
    str1= ""
    for i in range(len(myList)):
        if(i == len(myList)-1):
            str1=str1+"and "+ myList[i];
        else:
            str1=str1+myList[i] +", ";
    return str1
        