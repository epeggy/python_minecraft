# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:12:36 2020

@author: ASUS
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

mc.postToChat("i will watch you")
while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("at {},{},{}".format(x,y,z)) 
    mc.setBlock(x,y-1,z,103)