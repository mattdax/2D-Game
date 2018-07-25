import pyglet
from game import Game
class mainmenu():
	def __init__(self):
		self.height = 2048//4
		self.width = 2048//2
		
		self.MenuWindow = pyglet.window.Window(width=self.width, height=self.height,visible=True)
		self.logoLoad = pyglet.image.load('assets\\Name.png')
		self.logo = pyglet.sprite.Sprite(self.logoLoad,x=self.width//4,y=340)
		self.logo.update(scale_y=0.75,scale_x=0.75)
		self.bgLoad=pyglet.image.load("assets\\MainMenu.png")
		
		self.bg = pyglet.sprite.Sprite(self.bgLoad,x=0,y=0)
		self.playButtonLoad = pyglet.image.load("assets\\PlayButton.png")
		self.exitButtonLoad = pyglet.image.load("assets\\ExitButton.png")
		self.optionsButtonLoad = pyglet.image.load("assets\\OptionsButton.png")

		self.cur = 1

		self.keys = pyglet.window.key.KeyStateHandler()
		self.MenuWindow.push_handlers(self.keys)


		self.Button = pyglet.sprite.Sprite(self.playButtonLoad,x=0,y=0)
		self.on_key_press = self.MenuWindow.event(self.on_key_press)
		self.on_draw = self.MenuWindow.event(self.on_draw)
		

		self.createLabels()
		

		pyglet.app.run()

	
	def createLabels(self):
		self.play = pyglet.text.Label("Play",font_size=30,
                         x=self.width//2, y=320,color=(000,000,000,200),anchor_x='center', anchor_y='top')
		self.options = pyglet.text.Label("Options",font_size=30,
                         x=self.width//2, y=260,color=(000,000,000,200),anchor_x='center', anchor_y='top')
		self.exit = pyglet.text.Label("Exit",font_size=30,
                         x=self.width//2, y=200,color=(000,000,000,200),anchor_x='center', anchor_y='top')
	def button(self):
		if self.cur ==1:
			self.Button = pyglet.sprite.Sprite(self.playButtonLoad,x=0,y=0)
		elif self.cur==2:
			self.Button= pyglet.sprite.Sprite(self.optionsButtonLoad,x=0,y=0)
		else:
			self.Button= pyglet.sprite.Sprite(self.exitButtonLoad,x=0,y=0)

	def check(self):
		if self.cur == 1:
			return Game()
			
		if self.cur == 3:
			return exit()
	def on_key_press(self,symbol,modifiers):
		if symbol == pyglet.window.key.UP:
			if self.cur == 1:
				pass
			else:
				self.cur -=1
				self.button()
		elif symbol == pyglet.window.key.DOWN:
			if self.cur == 3:
				pass
			else:
				self.cur +=1
				self.button()
		elif symbol == pyglet.window.key.ENTER:
			self.check()


	def on_draw(self):
		self.bg.draw()
		self.logo.draw()
		self.play.draw()
		self.options.draw()
		self.exit.draw()
		self.Button.draw()


mainmenu()

