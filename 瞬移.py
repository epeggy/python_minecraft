# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:40:45 2020

@author: ASUS
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

mc.postToChat("i will watch you")
while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("at {},{},{}".format(x,y,z)) 

