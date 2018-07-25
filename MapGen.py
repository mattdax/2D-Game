from PIL import Image
from random import randint
def gen():
	#opens an image:
	Grass = Image.open("assets\\Grass.png")
	Water = Image.open("assets\\Water2.0.png")
	#creates a new empty image, RGB mode, and size 400 by 400.
	Map = Image.new('RGB', (2048,2048))

	#Creates the map
	status = {}
	for x in range(0,33,1):
		status [x]={}
		for y in range(0,33,1):
			status[x][y] = 0

	for x in range (1,33,1):
		for y in range (1,33,1):
			if status[x-1][y]==2:
				status[x][y] = randint(1,2)
			else:
				status[x][y] = randint(1,6)
	status[8][4] = 1
	
	#Iterate through a 4 by 4 grid with 100 spacing, to place my image
	for i in range(0,2112,64):
	    for j in range(0,2112,64):
	        #I change brightness of the images, just to emphasise they are unique copies.
	        #paste the image at location i,j:
	        if status[i//64][j//64]==2:
	        	Map.paste(Water, (i,j))
	        else:
	        	Map.paste(Grass, (i,j))
	
	Map.save("assets\\Map.png")
	return status

gen()