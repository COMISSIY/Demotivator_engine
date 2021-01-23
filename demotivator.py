
class App:
	def __init__(self):
		self.SC = pygame.display.set_mode((600, 400))
		self.d = Demotivator()

	def run(self):
		while True:
			self.event()
			self.draw()

	def draw(self):
		self.SC.fill((0, 0, 0))
		self.d.return_image()
		pygame.display.update()

	def event(self):
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				exit()

class Demotivator:
	def __init__(self):
		root = Tk()
		root.overrideredirect(1)
		root.withdraw()
		self.path = filedialog.askopenfilename()
		self.main_image = pygame.transform.scale(pygame.image.load(self.path), (400, 250))
		self.collide = self.main_image.get_rect(center=(300, 140))
		root.destroy()
		self.font1 = pygame.font.SysFont("Times New Roman", 40)
		self.font2 = pygame.font.Font(None, 25)
		self.inp = "Hi"#first_line
		self.inp2 = "Demotivator"#second_line
		self.text = self.font1.render(self.inp, True, (255, 255, 255))
		self.text2 = self.font2.render(self.inp2, True, (255, 255, 255))
		self.text_collide = self.text.get_rect(center=(300, 300))
		self.text_collide2 = self.text2.get_rect(center=(300, 350))

	def return_image(self):
		app.SC.blit(self.main_image, self.collide)
		pygame.draw.rect(app.SC, (255, 255, 255), (self.collide.x-5, self.collide.y-5, self.collide.width+10, self.collide.height+10), 3)
		app.SC.blit(self.text, self.text_collide)
		app.SC.blit(self.text2, self.text_collide2)

if __name__ == '__main__':
	from tkinter import *
	from tkinter import filedialog
	import pygame
	pygame.init()
	app = App()
	app.run()