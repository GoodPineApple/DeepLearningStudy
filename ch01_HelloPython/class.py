# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:40:29 2017

@author: taemi
"""

class Man:
    def __init__(self,name):
        self.name = name 
        print("intialized!")
        
    def hello(self):
        print("Hello "+self.name + "!")
        
    def goodbye(self):
        print("goodbye")
        
m = Man("David")
m.hello()
m.goodbye()