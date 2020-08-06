# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:26:47 2020

@author: ASUS
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y-1,z,46)