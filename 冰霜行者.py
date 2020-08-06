import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
while :
    x,y,z = mc.player.getTilePos()
    a=mc.getBlock(x,y-1,z+1)
    b=mc.getBlock(x,y-1,z-1)
    c=mc.getBlock(x+1,y-1,z)
    d=mc.getBlock(x-1,y-1,z)
    e=mc.getBlock(x,y-1,z)
    time.sleep(0.1)
    if a==9 or b==9 or c==9 or d==9 or e==9:
        mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,57)