from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
for i in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+i
    for j in range(10):
        r = random.randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,r)
r=random.randrange(1,16) 
data=0
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        block=mc.getBlockWithData(hit.pos)
        data=block.data
    if data==r:
        mc.postToChat("you find it")
    
        
