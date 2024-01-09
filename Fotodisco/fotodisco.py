import pygame, random
from random import randint


WIDTH = 800
HEIGHT = 650
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
#GREEN = (0, 255, 0)
#RED = (255,0,0)
#BLUE = (0,0,255)
#BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fotodisco")
clock = pygame.time.Clock()

def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

class Box1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[4] # latano
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 240
		self.rect.centery = 250

	def update(self):

		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			num1 = randint(1,328)
			if num1 == 1:
				self.image = box_images[8] # hpotion
			if num1 == 2:
				self.image = box_images[9] # mpotion
			if num1 == 3:
				self.image = box_images[10] # revive
			if num1 == 4:
				self.image = box_images[11] # mrevive
			if num1 >= 5 and num1 <= 230:
				self.image = box_images[0] # pokeb
			if num1 >= 231 and num1 <= 243:
				self.image = box_images[2] # ultrab
			if num1 >= 244 and num1 <= 284:
				self.image = box_images[1] # superb
			if num1 >= 285 and num1 <= 297:
				self.image = box_images[5] # piña
			if num1 >= 298 and num1 <= 309:
				self.image = box_images[3] # latano
			if num1 >= 310 and num1 <= 322:
				self.image = box_images[3] # frambu
			if num1 >= 323 and num1 <= 325:
				self.image = box_images[6] # potion
			if num1 >= 326 and num1 <= 328:
				self.image = box_images[7] # spotion
			
			
class Box2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[2] # ultrab
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 400
		self.rect.centery = 250

	def update(self):

		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			num1 = randint(1,328)
			if num1 == 1:
				self.image = box_images[8] # hpotion
			if num1 == 2:
				self.image = box_images[9] # mpotion
			if num1 == 3:
				self.image = box_images[10] # revive
			if num1 == 4:
				self.image = box_images[11] # mrevive
			if num1 >= 5 and num1 <= 230:
				self.image = box_images[0] # pokeb
			if num1 >= 231 and num1 <= 243:
				self.image = box_images[2] # ultrab
			if num1 >= 244 and num1 <= 284:
				self.image = box_images[1] # superb
			if num1 >= 285 and num1 <= 297:
				self.image = box_images[5] # piña
			if num1 >= 298 and num1 <= 309:
				self.image = box_images[3] # latano
			if num1 >= 310 and num1 <= 322:
				self.image = box_images[3] # frambu
			if num1 >= 323 and num1 <= 325:
				self.image = box_images[6] # potion
			if num1 >= 326 and num1 <= 328:
				self.image = box_images[7] # spotion

class Box3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[3] # frambu
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 560
		self.rect.centery = 250

	def update(self):

		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			num1 = randint(1,328)
			if num1 == 1:
				self.image = box_images[8] # hpotion
			if num1 == 2:
				self.image = box_images[9] # mpotion
			if num1 == 3:
				self.image = box_images[10] # revive
			if num1 == 4:
				self.image = box_images[11] # mrevive
			if num1 >= 5 and num1 <= 230:
				self.image = box_images[0] # pokeb
			if num1 >= 231 and num1 <= 243:
				self.image = box_images[2] # ultrab
			if num1 >= 244 and num1 <= 284:
				self.image = box_images[1] # superb
			if num1 >= 285 and num1 <= 297:
				self.image = box_images[5] # piña
			if num1 >= 298 and num1 <= 309:
				self.image = box_images[3] # latano
			if num1 >= 310 and num1 <= 322:
				self.image = box_images[3] # frambu
			if num1 >= 323 and num1 <= 325:
				self.image = box_images[6] # potion
			if num1 >= 326 and num1 <= 328:
				self.image = box_images[7] # spotion

class Box4(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[0]# pokeb
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 100

	def update(self):
		pass
		
class Box5(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[1] # superb
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box6(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[2] # ultrab
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box7(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[3] # frambu
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box8(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[4] # latano
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box9(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[5] # piña
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box10(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[6] # potion
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box11(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[7] # spotion
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box12(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[8] # hpotion
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box13(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[9] # mpotion
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box14(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[10] # revive
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

class Box15(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = box_images[11] # revivem
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 200

	def update(self):
		pass

def show_go_screen():
	
	screen.fill(BLACK)#background, [0,0])
	draw_text(screen, "Fotodisco", 65, WIDTH // 2, HEIGHT // 4)
	draw_text(screen, "xxx", 20, WIDTH // 2, HEIGHT * 3/7)
	draw_text(screen, "xxx", 20, WIDTH // 2, HEIGHT * 4/8)
	draw_text(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

box_images = []
box_list1 = ["img/pokeb.png", "img/superb.png", "img/ultrab.png", "img/frambu.png",
				"img/latano.png" , "img/piña.png", "img/potion.png", "img/spotion.png", 
				"img/hpotion.png", "img/mpotion.png", "img/revive.jpg", "img/revivem.png"]

for img in box_list1:
	box_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(85,85)))

background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(800,650))

running = True
pokeb = 0
superb = 0
ultrab = 0
frambu = 0
latano = 0
piña = 0
potion = 0
spotion = 0
hpotion = 0
mpotion = 0
revive = 0
revivem = 0
start = True
while running:
	if start:

		show_go_screen()

		start = False
		screen.blit(background, [0,0])
		all_sprites = pygame.sprite.Group()
		box1 = Box1()
		box2 = Box2()
		box3 = Box3()
		box4 = Box4()#pokeb
		box5 = Box5()#superb
		box6 = Box6()# ultrab
		box7 = Box7()# frambu
		box8 = Box8()# latano
		box9 = Box9()# piña
		box10 = Box10()# potion
		box11 = Box11()# spotion
		box12 = Box12()# hpotion
		box13 = Box13()# mpotion
		box14 = Box14()# revive
		box15 = Box15()# revivem
		all_sprites.add(box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11, box12, box13, box14, box15)
				
		scounter = True
		counter = True
		score = 50
		payout = 0

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	if score == 0:
		game_over =True 
	
	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_f]:
		if scounter:
			#score -= 1
			#payout = 0
			scounter = False
		counter = True
	elif not keystate[pygame.K_f]:
		scounter = True
		if counter:
			if box1.image == box_images[0]: # pokeb
				pokeb += 1
				#payout = 6
				counter = False
			if box1.image == box_images[1]: # superb
				superb += 1
				#payout = 8
				counter = False
			if box1.image == box_images[2]: # ultrab
				ultrab += 1
				#payout = 10
				counter = False
			if box1.image == box_images[3]: # frambu
				frambu += 1
				#payout = 15
				counter = False
			if box1.image == box_images[4]: # latano
				latano += 1
				#payout = 50
				counter = False
			if box1.image == box_images[5]: #  piña
				piña += 1
				#payout = 300
				counter = False
			if box1.image == box_images[6]: #  potion
				potion += 1
				#payout = 300
				counter = False
			if box1.image == box_images[7]: #  spotion
				spotion += 1
				#payout = 300
				counter = False
			if box1.image == box_images[8]: #  hpotion
				hpotion += 1
				#payout = 300
				counter = False
			if box1.image == box_images[9]: #  mpotion
				mpotion += 1
				#payout = 300
				counter = False
			if box1.image == box_images[10]: #  revive
				revive += 1
				#payout = 300
				counter = False
			if box1.image == box_images[11]: #  revivem
				revivem += 1
				#payout = 300
				counter = False
			if box2.image == box_images[0]: # pokeb
				pokeb += 1
				#payout = 6
				counter = False
			if box2.image == box_images[1]: # superb
				superb += 1
				#payout = 8
				counter = False
			if box2.image == box_images[2]: # ultrab
				ultrab += 1
				#payout = 10
				counter = False
			if box2.image == box_images[3]: # frambu
				frambu += 1
				#payout = 15
				counter = False
			if box2.image == box_images[4]: # latano
				latano += 1
				#payout = 50
				counter = False
			if box2.image == box_images[5]: #  piña
				piña += 1
				#payout = 300
				counter = False
			if box2.image == box_images[6]: #  potion
				potion += 1
				#payout = 300
				counter = False
			if box2.image == box_images[7]: #  spotion
				spotion += 1
				#payout = 300
				counter = False
			if box2.image == box_images[8]: #  hpotion
				hpotion += 1
				#payout = 300
				counter = False
			if box2.image == box_images[9]: #  mpotion
				mpotion += 1
				#payout = 300
				counter = False
			if box2.image == box_images[10]: #  revive
				revive += 1
				#payout = 300
				counter = False
			if box2.image == box_images[11]: #  revivem
				revivem += 1
				#payout = 300
				counter = False
			if box3.image == box_images[0]: # pokeb
				pokeb += 1
				#payout = 6
				counter = False
			if box3.image == box_images[1]: # superb
				superb += 1
				#payout = 8
				counter = False
			if box3.image == box_images[2]: # ultrab
				ultrab += 1
				#payout = 10
				counter = False
			if box3.image == box_images[3]: # frambu
				frambu += 1
				#payout = 15
				counter = False
			if box3.image == box_images[4]: # latano
				latano += 1
				#payout = 50
				counter = False
			if box3.image == box_images[5]: #  piña
				piña += 1
				#payout = 300
				counter = False
			if box3.image == box_images[6]: #  potion
				potion += 1
				#payout = 300
				counter = False
			if box3.image == box_images[7]: #  spotion
				spotion += 1
				#payout = 300
				counter = False
			if box3.image == box_images[8]: #  hpotion
				hpotion += 1
				#payout = 300
				counter = False
			if box3.image == box_images[9]: #  mpotion
				mpotion += 1
				#payout = 300
				counter = False
			if box3.image == box_images[10]: #  revive
				revive += 1
				counter = False
			if box3.image == box_images[11]: #  revivem
				revivem += 1
				counter = False
				
	all_sprites.update()

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	
	draw_text(screen,"pokeball: " + str(pokeb), 20, 700, 50)
	draw_text(screen,"superball: " + str(superb), 20, 700, 70)
	draw_text(screen, "ultraball: " + str(ultrab), 20, 700, 90)
	draw_text(screen, "frambu: " + str(frambu), 20, 700, 120)
	draw_text(screen, "latano: " + str(latano), 20, 700, 140)
	draw_text(screen, "piña " + str(piña), 20, 700, 160)
	draw_text(screen, "potion " + str(potion), 20, 700, 190)
	draw_text(screen,  "superpotion: " + str(spotion), 20, 700, 210)
	draw_text(screen,  "hiperpotion: " + str(hpotion), 20, 700, 230)
	draw_text(screen,  "maxpotion: " + str(mpotion), 20, 700, 250)
	draw_text(screen,  "revive: " + str(revive), 20, 700, 270)
	draw_text(screen,  "maxrevive: " + str(revivem), 20, 700, 290)

	pygame.display.flip()