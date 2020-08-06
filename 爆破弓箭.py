# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:46:42 2020

@author: ASUS
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
#mc.createExplosion(x,y,z)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlock(x,y,z,145)
        