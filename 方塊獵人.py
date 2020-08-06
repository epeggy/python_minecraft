

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        ID=mc.getBlock(x,y,z)
        mc.postToChat("YOU GOT {}".format(ID))