import pyglet
class mainmenu():
	def __init__(self):
		self.height = 2048//4
		self.width = 2048//2
		self.GameWindow = pyglet.window.Window(width=self.width, height=self.height,visible=True)
		self.logoLoad = pyglet.image.load('assets\\Name.png')
		self.logo = pyglet.sprite.Sprite(self.logoLoad,x=self.width//4,y=340)
		self.logo.update(scale_y=0.75,scale_x=0.75)
		self.bgLoad=pyglet.image.load("assets\\MainMenu.png")
		self.bg = pyglet.sprite.Sprite(self.bgLoad,x=0,y=0)
		self.playButtonLoad = pyglet.image.load("assets\\PlayButton.png")
		self.playButton = pyglet.sprite.Sprite(self.playButtonLoad,x=0,y=0)

		self.on_draw = self.GameWindow.event(self.on_draw)
		self.createLabels()
		pyglet.app.run()

	
	def createLabels(self):
		self.play = pyglet.text.Label("Play",font_size=30,
                         x=self.width//2, y=320,color=(000,000,000,200),anchor_x='center', anchor_y='top')
		self.options = pyglet.text.Label("Options",font_size=30,
                         x=self.width//2, y=260,color=(000,000,000,200),anchor_x='center', anchor_y='top')
		self.exit = pyglet.text.Label("Exit",font_size=30,
                         x=self.width//2, y=200,color=(000,000,000,200),anchor_x='center', anchor_y='top')




	def on_draw(self):
		self.bg.draw()
		self.logo.draw()
		self.play.draw()
		self.options.draw()
		self.exit.draw()
		self.playButton.draw()


mainmenu()


#TODO:
#
#2. selection rectangle
#3. enter(key) selects the option
#
#