# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:08:52 2020

@author: ASUS
"""
import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.createExplosion(x,y,z,5)
while True:
    x,y,z=mc.player.getTilePos()
    mc.createExplosion(x,y,z,5)
    time.sleep(1)