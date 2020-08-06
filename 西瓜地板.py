# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:53:05 2020

@author: ASUS
"""
import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
time.sleep(5)
x,y,z = mc.player.getTilePos()
mc.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,103)
