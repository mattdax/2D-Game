from PIL import Image
from random import randint
def outGen():
	#opens an image:
	Outside = Image.open("Black.png")
	#creates a new empty image, RGB mode, and size 400 by 400.
	Map = Image.new('RGB', (2048,2048))

	#Creates the map
	status = {}
	for x in range (0,33):
		status [x]={}
		for y in range (0,33):
			status[x][y] = 1
	for i in range(0,2112,64):
	    for j in range(0,2112,64):
	        #I change brightness of the images, just to emphasise they are unique copies.
	        #paste the image at location i,j:
	        	Map.paste(Outside, (i,j))
	Map.save("Outside.png")
outGen()