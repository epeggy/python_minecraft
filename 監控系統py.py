
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
mc.postToChat("i watching you")
while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("at {} , {} ,{}".format(x,y,z))

