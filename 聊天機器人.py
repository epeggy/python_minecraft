

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

try:
    block=int(input("請輸入方塊ID"))
    mc.setBlock(x,y,z,block)
except:
    print("只能輸入數字")