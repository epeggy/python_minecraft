from mcpi.minecraft import Minecraft
mc = Minecraft.create()
list2d=[[14,15,16],
        [56,73,129]]
myID=mc.getPlayerEntityIds()
x,y,z=mc.entity.getTilePos(myID)
startx=x
for list1d in list2d:
    for i in list1d:
        mc.setBlock(x,y,z,i)
        x=x+1
    x=startx
    z=z+1

