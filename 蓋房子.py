

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlocks(x+5,y+5,z+5,x-5,y-5,z-5,57)
mc.setBlocks(x+4,y+4,z+4,x-4,y-4,z-4,0)
