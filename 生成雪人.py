from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
time.sleep(5)
x,y,z = mc.player.getTilePos()
number=1
for i in range(4):
    for j in range(number):
        mc.setBlock(x,y,z,80)
        mc.setBlock(x,y+1,z,80)
        mc.setBlock(x,y+2,z,86)
    number=number*2       
mc.postToChat('there are lot of snow man')
