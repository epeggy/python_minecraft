from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def py(x,y,z):
    base = 10
    height =(base//2)+1
    for i in range(height):
        x1=x+i
        y1=y+i
        z1=z+i
        x2=x+base-i
        z2=z+base-i
        mc.setBlocks(x1,y1,z1,x2,y1,z2,24)
x,y,z = mc.player.getTilePos()
py(x,y,z)
