import pyglet
from MapGen import gen
class Game():
	def __init__(self):
		self.height = 2048//4
		self.width = 2048//2
		
		#Create Variables
		self.playerLocationX=0
		self.playerLocationY=0
		
		self.directionX = 0
		self.directionY = 0


		#Creates the window
		#TODO: Find Name
		self.GameWindow = pyglet.window.Window(width=self.width, height=self.height,visible=True)
		

		#Setting up keys
		self.keys = pyglet.window.key.KeyStateHandler()
		self.GameWindow.push_handlers(self.keys)

		#Window events go here
		self.on_draw = self.GameWindow.event(self.on_draw)
		self.on_text_motion = self.GameWindow.event(self.on_text_motion)
		
		#Map Gen func call
		self.mapGen()

		#Window Loop
		pyglet.app.run()
		
	#Calls Different File		
	def mapGen(self):
		self.map = gen()
		self.loadImages()

		#Loads the created map, and character
	def loadImages(self):
		self.GameWindow.clear()
		
		self.outLoad=pyglet.image.load("Outside.png")
		self.OutsideBot = pyglet.sprite.Sprite(self.outLoad,y=-1200,x=-1024)
		#self.OutsideRight = pyglet.sprite.Sprite(self.outLoad,y=0,x=-1600)
		#self.OutsideLeft = pyglet.sprite.Sprite(self.outLoad,y=0,x=-1500)
		
		#Map Load
		self.mapLoad = pyglet.image.load("Map.png")
		self.Map = pyglet.sprite.Sprite(self.mapLoad,y=0,x=0)
		
		#Player Spawn Location
		self.playerLocationX = self.Map.x+(self.width//2)+1024-2048
		self.playerLocationY = self.Map.y+(self.height//2)+2048-2560
		
		#Player image load
		self.p1Load = pyglet.image.load("p1.png")
		self.Player = pyglet.sprite.Sprite(self.p1Load,y=self.height//2,x=self.width//2)
	
	def updatePlayerLocation(self):
		#self.oldLocationX = self.playerLocationX
		#self.oldLocationY = self.playerLocationY
		self.playerLocationX = self.Map.x+(self.width//2)+1024-2048
		self.playerLocationY = self.Map.y+(self.height//2)+2048-2560
		#self.checkIfWater()

	#Checks if player is running into water	
	def checkIfWater(self):
		if self.map[int(int(self.playerLocationX+(self.directionX))/64)*-1][-1*(-1*int(int(((self.playerLocationY-64+(self.directionY))))/64)-32)] == 2:
			return True
	
	#Draws map and player onto the window
	def on_draw(self):
		self.OutsideBot.draw()
		self.Map.draw()
		self.Player.draw()

		#For Moving
	def on_text_motion(self,motion):
		if(motion == pyglet.window.key.MOTION_UP):
			if self.Map.y-64<=-1760:
				self.Map.y=-1760
			else:
				self.directionY = -64
				if self.checkIfWater() == True:
					pass
				else:
					self.Map.y-=64
				self.directionY = 0
			#print("Player:"+str(self.playerLocationX)+","+str(self.playerLocationY))
			#print("Map:"+str(self.Map.x)+","+str(self.Map.y))
		if(motion == pyglet.window.key.MOTION_DOWN):
			if self.Map.y+64>=0+(self.height//2):
				self.Map.y=0+(self.height//2)
			else:
				self.directionY = 64
				if self.checkIfWater() == True:
					pass
				else:
					self.Map.y+=64
				self.directionY = 0
			#print("Player:"+str(self.playerLocationX)+","+str(self.playerLocationY))
			#print("Map:"+str(self.Map.x)+","+str(self.Map.y))
		if(motion == pyglet.window.key.MOTION_LEFT):
			if self.Map.x+64>=0+(self.width//2):
				self.Map.x=0+(self.width//2)
			else:
				self.directionX = 64
				if self.checkIfWater() == True:
					pass
				else:
					self.Map.x+=64
				self.directionX = 0
			
			#print("Player:"+str(self.playerLocationX)+","+str(self.playerLocationY))
			#print("Map:"+str(self.Map.x)+","+str(self.Map.y))
		if(motion == pyglet.window.key.MOTION_RIGHT):
			if self.Map.x-64<=-1472:
				self.oldLocationX = self.Map.x
				self.Map.x=-1472
			else:
				self.directionX = -64
				if self.checkIfWater() == True:
					pass
				else:
					self.Map.x-=64
				self.directionX = 0
			#print("Player:"+str(self.playerLocationX)+","+str(self.playerLocationY))
			print("Map:"+str(self.Map.x)+","+str(self.Map.y))
		self.updatePlayerLocation()
		
		#DONT DELETE FOR BUG FIXING
		print((self.playerLocationX//64)*-1,-1*((self.playerLocationY)//64))
		print(self.map[(self.playerLocationX//64)*-1][-1*((self.playerLocationY)//64)])

Game()