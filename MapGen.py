from PIL import Image
from random import randint
def gen():
	#opens an image:
	Grass = Image.open("assets\\Green.png")
	Water = Image.open("assets\\Blue.png")
	#creates a new empty image, RGB mode, and size 400 by 400.
	Map = Image.new('RGB', (2048,2048))

	#Creates the map
	status = {}
	for x in range (0,33):
		status [x]={}
		for y in range (0,33):
			status[x][y] = randint(1,3)
	status[8][4]=1
	status[4][8]=1
	status[8][5]=1
	#Here I resize my opened image, so it is no bigger than 100,100
	
	#Iterate through a 4 by 4 grid with 100 spacing, to place my image
	for i in range(0,2112,64):
	    for j in range(0,2112,64):
	        #I change brightness of the images, just to emphasise they are unique copies.
	        #paste the image at location i,j:
	        if status[i//64][j//64]==1 or status[i//64][j//64]==3:
	        	Map.paste(Grass, (i,j))
	        if status[i//64][j//64]==2:
	        	Map.paste(Water, (i,j))
	Map.save("assets\\Map.png")
	return status