from mcpi.minecraft import Minecraft
mc = Minecraft.create()
line1=[]
line2=[]
line3=[]
for i in range(1,4):
    line1.append(1*i)
for i in range(1,4):
    line2.append(2*i)
for i in range(1,4):
    line3.append(3*i)
mc.postToChat(line1)
mc.postToChat(line2)
mc.postToChat(line3)
