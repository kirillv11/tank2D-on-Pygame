import pygame
from time import ctime
from map import create_map, img_grass, img_rect_grass, num_of_map


class Player:
	def __init__( self, x_direction, y_direction, tank_direction, speed, health, speed_shot, count_patron):
		self.x = x_direction
		self.y = y_direction
		self.tank_direction = tank_direction
		self.count_patron = count_patron
		self.health = health
		self.speed = speed
		self.patron = []
		self.img_patron = pygame.image.load("img\\other\\patron\\patron.png")
		self.speed_shot = speed_shot

	def up( self ):  # go up
		if self.y >= 0:
			self.y -= self.speed

	def down( self ):  # go down
		if self.y < 620:
			self.y += self.speed

	def right( self ):  # go right
		if self.x < 1320:
			self.x += self.speed

	def left( self ):  # go left
		if self.x >= 0:
			self.x -= self.speed

	def draw( self, adress ):
		"""this function is responsible for rendering the player"""
		adress.set_colorkey((255, 255, 255))
		screen.blit(adress, (self.x, self.y))

	def shot( self, direction, types ):
		"""the function is responsible for shots"""
		if types == 1:
			if direction == "right":
				patron_rect = pygame.Rect(self.x + 75, self.y + 26, 14, 14)
				self.patron.append([patron_rect, direction])
			if direction == "left":
				patron_rect = pygame.Rect(self.x - 12, self.y + 26, 14, 14)
				self.patron.append([patron_rect, direction])
			if direction == "up":
				patron_rect = pygame.Rect(self.x + 26, self.y - 12, 14, 14)
				self.patron.append([patron_rect, direction])
			if direction == "down":
				patron_rect = pygame.Rect(self.x + 26, self.y + 75, 14, 14)
				self.patron.append([patron_rect, direction])
		if types == 2:
			if direction == "right":
				patron_rect = pygame.Rect(self.x + 100, self.y + 34, 14, 14)
				self.patron.append([patron_rect, direction])
			if direction == "left":
				patron_rect = pygame.Rect(self.x, self.y + 32, 14, 14)
				self.patron.append([patron_rect, direction])
			if direction == "up":
				patron_rect = pygame.Rect(self.x + 34, self.y, 14, 14)
				self.patron.append([patron_rect, direction])
			if direction == "down":
				patron_rect = pygame.Rect(self.x + 32, self.y + 100, 14, 14)
				self.patron.append([patron_rect, direction])

	def shot_draw( self ):
		for patron_object in self.patron:
			del_flag = False
			if patron_object[1] == 'right':
				if patron_object[0].x < 1382:
					patron_object[0].x += self.speed_shot
				else:
					del_flag = True
			if patron_object[1] == 'left':
				if patron_object[0].x > 0:
					patron_object[0].x -= self.speed_shot
				else:
					del_flag = True
			if patron_object[1] == 'up':
				if patron_object[0].y > 0:
					patron_object[0].y -= self.speed_shot
				else:
					del_flag = True
			if patron_object[1] == 'down':
				if patron_object[0].y < 682:
					patron_object[0].y += self.speed_shot
				else:
					del_flag = True

			if not del_flag:
				for rect in img_rect:
					if rect.colliderect(patron_object[0]):
						del_flag = True

			if del_flag:
				self.patron.remove(patron_object)
			else:
				screen.blit(self.img_patron, patron_object[0])


def menu():
	screen.blit(logo, (0, 0))
	pygame.display.flip()
	print("Write a number of your tank (1 - 4)")
	technic_firstplayer = input("1 player: ")
	technic_secondplayer = input("2 player: ")
	if not technic_firstplayer.isdigit() or not technic_secondplayer.isdigit():
		technic_firstplayer = 1
		technic_secondplayer = 1
	else:
		technic_firstplayer = int(technic_firstplayer)
		technic_secondplayer = int(technic_secondplayer)
	return technic_firstplayer, technic_secondplayer


pygame.init()
width, height = 1400, 850  # ширина, высота
screen = pygame.display.set_mode((width, height))

# FPS
clock = pygame.time.Clock()
FPS = 60

# settings
fx, fy, sx, sy = 0, 0, 1300, 600
go, go_enemy = 0, 0
#position = "right"
#position_enemy = "left"

info = pygame.image.load("interface\\Info.png")
hp = pygame.image.load("interface\\Jisn.png")
snarad = pygame.image.load("interface\\Snarad.png")

box = pygame.image.load("img\\texture\\box.png")
wall = pygame.image.load("img\\texture\\wall.png")
grass = pygame.image.load("img\\texture\\grass.png")
water = pygame.image.load("img\\texture\\Minecraft-Water.jpg")
logo = pygame.image.load("img\\logo.png")

# здесь номер карты
map: str = ""
pygame.mixer.init()

# настройка музыки
volume = 0.5
pygame.mixer.music.load("img\\texture\\Intro.mp3")
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(loops = -1)

technic_firstplayer, technic_secondplayer = menu()  # отрисовка меню

tank_first_player_top = pygame.image.load("img\\firstplayer\\Tank-" + str(technic_firstplayer) + "_1pl.png")
tank_first_player_bottom = pygame.image.load("img\\firstplayer\\Tank-" + str(technic_firstplayer) + "_1pl_d.png")
tank_first_player_right = pygame.image.load("img\\firstplayer\\Tank-" + str(technic_firstplayer) + "_1pl_r.png")
tank_first_player_left = pygame.image.load("img\\firstplayer\\Tank-" + str(technic_firstplayer) + "_1pl_l.png")

tank_second_player_top = pygame.image.load("img\\secondplayer\\Tank-" + str(technic_secondplayer) + "_2pl.png")
tank_second_player_bottom = pygame.image.load("img\\secondplayer\\Tank-" + str(technic_secondplayer) + "_2pl_d.png")
tank_second_player_right = pygame.image.load("img\\secondplayer\\Tank-" + str(technic_secondplayer) + "_2pl_r.png")
tank_second_player_left = pygame.image.load("img\\secondplayer\\Tank-" + str(technic_secondplayer) + "_2pl_l.png")
volumee = 0.7

if num_of_map == '1':
	pygame.mixer.music.load("snd\\Map1_battle.mp3")
	pygame.mixer.music.set_volume(volumee)
	pygame.mixer.music.play(loops = -1)
	map_fill = pygame.image.load("img\\texture\\As.jpg")
if num_of_map == '2':
	pygame.mixer.music.load("snd\\Map2_battle.mp3")
	pygame.mixer.music.set_volume(volumee)
	pygame.mixer.music.play(loops = -1)
	map_fill = pygame.image.load("img\\texture\\Grass.jpg")
if num_of_map == '3':
	pygame.mixer.music.load("snd\\Map3_battle.mp3")
	pygame.mixer.music.set_volume(volumee)
	pygame.mixer.music.play(loops = -1)
	map_fill = pygame.image.load("img\\texture\\Grass.jpg")

destruction = pygame.mixer.Sound("snd\\Probitie.mp3")
shot = pygame.mixer.Sound("snd\\f4ee46bb060c102.mp3")
probitie = pygame.mixer.Sound("snd\\1.mp3")
shot.set_volume(volume)
destruction.set_volume(volume)
probitie.set_volume(volume)

pygame.mixer.Channel(0).play(pygame.mixer.Sound("snd\\zvuk-zavedennogo-tanka-motora-12255.mp3"))
pygame.mixer.Channel(0).set_volume(0.15)

move_up, move_down, move_right, move_left = False, False, False, False
move_up_enemy, move_down_enemy, move_right_enemy, move_left_enemy = False, False, False, False

# инициализация классов
FirstPlayer = Player(fx, fy, 'right', 2, 5, 14, 12)
SecondPlayer = Player(sx, sy, 'left', 2, 5, 14, 12)

# создание коллизии
collision_first = pygame.Rect(FirstPlayer.x, FirstPlayer.y, tank_first_player_right.get_width(),
							  tank_second_player_right.get_height())
collision_second = pygame.Rect(SecondPlayer.x, SecondPlayer.y, tank_second_player_right.get_width(),
							   tank_second_player_right.get_height())
# очки
score_player = 0
score_player_enemy = 0

# объекты карты
img_rect = create_map()[0]
img = create_map()[1]

# Текст
font = pygame.font.SysFont('Consolas', 20)
per = font.render('Перезарядка', True, (255, 255, 255))
font_ready_player = pygame.font.SysFont('Consolas', 20)
ready_player = font_ready_player.render('Готово', True, (255, 255, 255))
font_ready_player_enemy = pygame.font.SysFont('Consolas', 20)
ready_player_enemy = font_ready_player.render('Готово', True, (255, 255, 255))

font_score = pygame.font.SysFont('Consolas', 40)
score = font_score.render(f"{str(score_player)} : {str(score_player_enemy)}", True, (255, 255, 255))

font_patron_ready_player = pygame.font.SysFont('Consolas', 20)
patron_ready_player = font_patron_ready_player.render('нет патрон', True, (255, 255, 255))
font_patron_ready_player_enemy = pygame.font.SysFont('Consolas', 20)
patron_ready_player_enemy = font_patron_ready_player_enemy.render('нет патрон', True, (255, 255, 255))


def conflict( direction, types):
	"""
		функции проверяющяя столкновения
	"""
	flag = False
	if types == 1:
		if direction == 'up':
			line_x, line_y = FirstPlayer.x + 32, FirstPlayer.y
			line_x_right, line_y_right = FirstPlayer.x + 60, FirstPlayer.y
			line_x_left, line_y_left = FirstPlayer.x, FirstPlayer.y

			line_y_before = FirstPlayer.y
			for i in range(0, 100):
				if flag:
					break
				if line_y_left < 0:
					break
				line_x -= 1
				line_y_right -= 1
				line_y_left -= 1
				line = pygame.Rect(line_x, line_y, 1, 1)
				line_right = pygame.Rect(line_x_right, line_y_right, 1, 1)
				line_left = pygame.Rect(line_x_left, line_y_left, 1, 1)
				if line.colliderect(collision_second) or \
						line_left.colliderect(collision_second) or \
						line_right.colliderect(collision_second):
					flag = True
				else:
					for j in img_rect:
						if line.colliderect(j) or line_left.colliderect(j) or line_right.colliderect(j):
							flag = True
							break
			if abs(int(line_y_before - line_y_right)) > 5:
				FirstPlayer.up()
		elif direction == 'down':
			line_x, line_y = FirstPlayer.x + 32, FirstPlayer.y + 75
			line_x_right, line_y_right = FirstPlayer.x + 64, FirstPlayer.y + 75
			line_x_left, line_y_left = FirstPlayer.x, FirstPlayer.y + 75

			line_y_before = FirstPlayer.y + 75
			line = pygame.Rect(line_x, line_y, 1, 1)
			s = []
			for i in range(0, 100):
				if flag:
					break
				if line_y > 700:
					break
				line_y += 1
				line_y_right += 1
				line_y_left += 1
				line = pygame.Rect(line_x, line_y, 1, 1)
				line_right = pygame.Rect(line_x_right, line_y_right, 1, 1)
				line_left = pygame.Rect(line_x_left, line_y_left, 1, 1)
				s.append(line_right)
				if line.colliderect(collision_second) or \
						line_left.colliderect(collision_second) or \
						line_right.colliderect(collision_second):
					flag = True
				else:
					for j in img_rect:
						if line.colliderect(j) or line_left.colliderect(j) or line_right.colliderect(j):
							flag = True
							break

			if abs(int(line_y_before - line_y_right)) > 25:
				FirstPlayer.down()
		elif direction == 'right':
			line_x, line_y = FirstPlayer.x + 80, FirstPlayer.y + 32
			line_x_right, line_y_right = FirstPlayer.x + 80, FirstPlayer.y
			line_x_left, line_y_left = FirstPlayer.x + 80, FirstPlayer.y + 60

			line_x_before = FirstPlayer.x + 26
			line = pygame.Rect(line_x, line_y, 1, 1)
			for i in range(0, 100):
				if flag:
					break
				if line_x > 1400:
					break
				line_x += 1
				line_x_right += 1
				line_x_left += 1
				line = pygame.Rect(line_x, line_y, 1, 1)
				line_right = pygame.Rect(line_x_right, line_y_right, 1, 1)
				line_left = pygame.Rect(line_x_left, line_y_left, 1, 1)
				if line.colliderect(collision_second) or \
						line_left.colliderect(collision_second) or \
						line_right.colliderect(collision_second):
					flag = True
				else:
					for j in img_rect:
						if line.colliderect(j) or line_left.colliderect(j) or line_right.colliderect(j):
							flag = True
							break

			if abs(int(line_x_before - line_x_right)) > 70:
				FirstPlayer.right()
		elif direction == 'left':
			line_x, line_y = FirstPlayer.x - 12, FirstPlayer.y + 32
			line_x_right, line_y_right = FirstPlayer.x - 12, FirstPlayer.y
			line_x_left, line_y_left = FirstPlayer.x - 12, FirstPlayer.y + 60

			line_x_before = FirstPlayer.x - 12
			line = pygame.Rect(line_x, line_y, 1, 1)
			for i in range(0, 100):
				if flag:
					break
				if line_x < 0:
					break
				line_x -= 1
				line_x_right += 1
				line_x_left += 1
				line = pygame.Rect(line_x, line_y, 1, 1)
				line_right = pygame.Rect(line_x_right, line_y_right, 1, 1)
				line_left = pygame.Rect(line_x_left, line_y_left, 1, 1)
				if line.colliderect(collision_second) or \
						line_left.colliderect(collision_second) or \
						line_right.colliderect(collision_second):
					flag = True
				else:
					for j in img_rect:
						if line.colliderect(j) or line_left.colliderect(j) or line_right.colliderect(j):
							flag = True
							break
			if abs(line_x_before - line_x) > 1 and abs(int(line_x_before - line_x_right)) > 1 and abs(
					int(line_x_before - line_x_left)) > 1:
				FirstPlayer.left()
				for i in img_rect:
					if collision_first.colliderect(i):
						FirstPlayer.x -= 0.01
						break
	elif types == 2:
		if direction == 'up':
			line_x, line_y = SecondPlayer.x + 38, SecondPlayer.y
			line_x_right, line_y_right = SecondPlayer.x + 80, SecondPlayer.y
			line_x_left, line_y_left = SecondPlayer.x, SecondPlayer.y

			line_y_before = SecondPlayer.y
			for i in range(0, 100):
				if flag:
					break
				if line_y < 0:
					break
				line_y -= 1
				line_y_right -= 1
				line_y_left -= 1
				line = pygame.Rect(line_x, line_y, 1, 1)
				line_right = pygame.Rect(line_x_right, line_y_right, 1, 1)
				line_left = pygame.Rect(line_x_left, line_y_left, 1, 1)
				if line.colliderect(collision_first) or \
						line_left.colliderect(collision_first) or \
						line_right.colliderect(collision_first):
					flag = True
				else:
					for j in img_rect:
						if line.colliderect(j) or line_left.colliderect(j) or line_right.colliderect(j):
							flag = True
							break
			if abs(int(line_y_before - line_y_right)) > 1:
				SecondPlayer.up()

		elif direction == 'down':
			line_x, line_y = SecondPlayer.x + 38, SecondPlayer.y + 100
			line_x_right, line_y_right = SecondPlayer.x + 79, SecondPlayer.y + 100
			line_x_left, line_y_left = SecondPlayer.x, SecondPlayer.y + 100

			line_y_before = SecondPlayer.y + 100
			for i in range(0, 100):
				if flag:
					break
				if line_y > 700:
					break
				line_y += 1
				line_y_right += 1
				line_y_left += 1
				line = pygame.Rect(line_x, line_y, 1, 1)
				line_right = pygame.Rect(line_x_right, line_y_right, 1, 1)
				line_left = pygame.Rect(line_x_left, line_y_left, 1, 1)
				if line.colliderect(collision_first) or \
						line_left.colliderect(collision_first) or \
						line_right.colliderect(collision_first):
					flag = True
				else:
					for j in img_rect:
						if line.colliderect(j) or line_left.colliderect(j) or line_right.colliderect(j):
							flag = True
							break
			if abs(int(line_y_before - line_y_right)) > 20:
				SecondPlayer.down()
		elif direction == 'right':
			line_x, line_y = SecondPlayer.x + 100, SecondPlayer.y + 38
			line_x_right, line_y_right = SecondPlayer.x + 100, SecondPlayer.y + 79
			line_x_left, line_y_left = SecondPlayer.x + 100, SecondPlayer.y

			line_x_before = SecondPlayer.x + 100
			for i in range(0, 100):
				if flag:
					break
				if line_x > 1400:
					break
				line_x += 1
				line_x_right += 1
				line_x_left += 1
				line = pygame.Rect(line_x, line_y, 1, 1)
				line_right = pygame.Rect(line_x_right, line_y_right, 1, 1)
				line_left = pygame.Rect(line_x_left, line_y_left, 1, 1)
				if line.colliderect(collision_first) or \
						line_left.colliderect(collision_first) or \
						line_right.colliderect(collision_first):
					flag = True
				else:
					for j in img_rect:
						if line.colliderect(j) or line_left.colliderect(j) or line_right.colliderect(j):
							flag = True
							break
			if abs(int(line_x_before - line_x_right)) > 20:
				SecondPlayer.right()
		elif direction == 'left':
			line_x, line_y = SecondPlayer.x + 15, SecondPlayer.y + 38
			line_x_right, line_y_right = SecondPlayer.x + 15, SecondPlayer.y + 79
			line_x_left, line_y_left = SecondPlayer.x + 15, SecondPlayer.y

			line_x_before = SecondPlayer.x + 15
			for i in range(0, 100):
				if flag:
					break
				if line_x < 0:
					break
				line_x -= 1
				line_x_right -= 1
				line_x_left -= 1
				line = pygame.Rect(line_x, line_y, 1, 1)
				line_right = pygame.Rect(line_x_right, line_y_right, 1, 1)
				line_left = pygame.Rect(line_x_left, line_y_left, 1, 1)
				if line.colliderect(collision_first) or \
						line_left.colliderect(collision_first) or \
						line_right.colliderect(collision_first):
					flag = True
				else:
					for j in img_rect:
						if line.colliderect(j) or line_left.colliderect(j) or line_right.colliderect(j):
							flag = True
							break
			if abs(int(line_x_before - line_x_right)) > 20:
				SecondPlayer.left()


# перезарядка
reload = 0
reload_enemy = 0
count1 = font.render(str(reload), True, (255, 255, 255))
count2 = font.render(str(reload_enemy), True, (255, 255, 255))
running = True
while running:
	clock.tick(FPS)

	# настройка перезарядки
	if reload != 300:
		reload += 1
	if reload_enemy != 300:
		reload_enemy += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				move_up = True
				go += 1
			if event.key == pygame.K_s:
				move_down = True
				go += 1
			if event.key == pygame.K_d:
				move_right = True
				go += 1
			if event.key == pygame.K_a:
				move_left = True
				go += 1
			if event.key == pygame.K_SPACE:  # стрельба
				if FirstPlayer.count_patron > 0 and reload == 300:
					FirstPlayer.shot(FirstPlayer.tank_direction, 1)
					FirstPlayer.count_patron -= 1
					shot.play()
					reload = 0
			if event.key == pygame.K_UP:
				move_up_enemy = True
				go_enemy += 1
			if event.key == pygame.K_DOWN:
				move_down_enemy = True
				go_enemy += 1
			if event.key == pygame.K_RIGHT:
				move_right_enemy = True
				go_enemy += 1
			if event.key == pygame.K_LEFT:
				move_left_enemy = True
				go_enemy += 1
			if event.key == pygame.K_p:  # пауза
				pygame.mixer.music.pause()
			if event.key == pygame.K_o:  # продолжение проигрывания
				pygame.mixer.music.unpause()
			if event.key == pygame.K_PAGEUP:  # регулировка громкости(громче)
				volume += 0.1
				shot.set_volume(volume)
				pygame.mixer.music.set_volume(volume)
			if event.key == pygame.K_PAGEDOWN:  # регулировка громкости(тише)
				volume -= 0.1
				shot.set_volume(volume)
				pygame.mixer.music.set_volume(volume)
		if event.type == pygame.MOUSEBUTTONDOWN:  # стрельба
			if event.button == 1:
				if SecondPlayer.count_patron > 0 and reload_enemy == 300:
					SecondPlayer.shot(SecondPlayer.tank_direction, 2)
					SecondPlayer.count_patron -= 1
					shot.play()
					reload_enemy = 0
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				move_up = False
				go -= 1
			if event.key == pygame.K_s:
				move_down = False
				go -= 1
			if event.key == pygame.K_d:
				move_right = False
				go -= 1
			if event.key == pygame.K_a:
				move_left = False
				go -= 1

			if event.key == pygame.K_UP:
				move_up_enemy = False
				go_enemy -= 1
			if event.key == pygame.K_DOWN:
				move_down_enemy = False
				go_enemy -= 1
			if event.key == pygame.K_RIGHT:
				move_right_enemy = False
				go_enemy -= 1
			if event.key == pygame.K_LEFT:
				move_left_enemy = False
				go_enemy -= 1

	screen.blit(map_fill, (0, 0))
	pygame.draw.rect(screen, [80, 80, 80], [0, 700, width, 150])

	# движение объектов
	if move_up and go == 1:
		FirstPlayer.tank_direction = 'up'
		conflict('up', 1)
	elif move_down and go == 1:
		FirstPlayer.tank_direction = 'down'
		conflict('down', 1)
	elif move_right and go == 1:
		FirstPlayer.tank_direction = 'right'
		conflict('right', 1)
	elif move_left and go == 1:
		FirstPlayer.tank_direction = 'left'
		conflict('left', 1)

	# rebirth
	if FirstPlayer.health <= 0:
		FirstPlayer.x, FirstPlayer.y = 0, 0
		FirstPlayer.health = 5
		FirstPlayer.count_patron = 12
		score_player_enemy += 1
	if SecondPlayer.health <= 0:
		SecondPlayer.x, SecondPlayer.y = 1300, 600
		SecondPlayer.health = 5
		SecondPlayer.count_patron = 12
		score_player += 1

	# drawing object
	if FirstPlayer.tank_direction == 'up':
		FirstPlayer.draw(tank_first_player_top)
		collision_first = pygame.Rect(FirstPlayer.x, FirstPlayer.y, tank_first_player_top.get_width(),
									  tank_second_player_top.get_height())
	elif FirstPlayer.tank_direction == 'down':
		FirstPlayer.draw(tank_first_player_bottom)
		collision_first = pygame.Rect(FirstPlayer.x, FirstPlayer.y, tank_first_player_bottom.get_width(),
									  tank_second_player_bottom.get_height())
	elif FirstPlayer.tank_direction == 'right':
		FirstPlayer.draw(tank_first_player_right)
		collision_first = pygame.Rect(FirstPlayer.x, FirstPlayer.y, tank_first_player_right.get_width(),
									  tank_second_player_right.get_height())
	elif FirstPlayer.tank_direction == 'left':
		FirstPlayer.draw(tank_first_player_left)
		collision_first = pygame.Rect(FirstPlayer.x, FirstPlayer.y, tank_first_player_left.get_width(),
									  tank_second_player_left.get_height())

	# движение объектов
	if move_up_enemy and go_enemy == 1:
		SecondPlayer.tank_direction = 'up'
		conflict('up', 2)
	elif move_down_enemy and go_enemy == 1:
		SecondPlayer.tank_direction = 'down'
		conflict('down', 2)
	elif move_right_enemy and go_enemy == 1:
		SecondPlayer.tank_direction = 'right'
		conflict('right', 2)
	elif move_left_enemy and go_enemy == 1:
		SecondPlayer.tank_direction = 'left'
		conflict('left', 2)

	# отрисовка объекта
	if SecondPlayer.tank_direction == 'up':
		SecondPlayer.draw(tank_second_player_top)
		collision_second = pygame.Rect(SecondPlayer.x, SecondPlayer.y, tank_second_player_top.get_width(),
									   tank_second_player_top.get_height())
	elif SecondPlayer.tank_direction == 'down':
		SecondPlayer.draw(tank_second_player_bottom)
		collision_second = pygame.Rect(SecondPlayer.x, SecondPlayer.y, tank_second_player_bottom.get_width(),
									   tank_second_player_bottom.get_height())
	elif SecondPlayer.tank_direction == 'right':
		SecondPlayer.draw(tank_second_player_right)
		collision_second = pygame.Rect(SecondPlayer.x, SecondPlayer.y, tank_second_player_right.get_width(),
									   tank_second_player_right.get_height())
	elif SecondPlayer.tank_direction == "left":
		SecondPlayer.draw(tank_second_player_left)
		collision_second = pygame.Rect(SecondPlayer.x, SecondPlayer.y, tank_second_player_left.get_width(),
									   tank_second_player_left.get_height())

	# drawing shots
	FirstPlayer.shot_draw()
	SecondPlayer.shot_draw()
	for obj in SecondPlayer.patron:
		if collision_first.colliderect(obj[0]):
			SecondPlayer.patron.remove(obj)
			FirstPlayer.health -= 1
			if FirstPlayer.health >= 1:
				probitie.play()
			else:
				destruction.play()
	for obj in FirstPlayer.patron:
		if collision_second.colliderect(obj[0]):
			FirstPlayer.patron.remove(obj)
			SecondPlayer.health -= 1
			if SecondPlayer.health >= 1:
				probitie.play()
			else:
				destruction.play()

	# drawing map
	for i in img_rect:
		if img[img_rect.index(i)] == "box":
			screen.blit(box, i)
		elif img[img_rect.index(i)] == "wall":
			screen.blit(wall, i)
		elif img[img_rect.index(i)] == "water":
			screen.blit(water, i)

	# drawing grass
	for i in img_rect_grass:
		if img_grass[img_rect_grass.index(i)] == "grass":
			screen.blit(grass, i)

	# отрисовка нижней части
	info.set_colorkey((255, 255, 255))
	hp.set_colorkey((255, 255, 255))
	screen.blit(info, (0, 700))

	# отображение элементов нижней панели
	steep = 0
	for i in range(FirstPlayer.health):
		screen.blit(hp, (130 + steep, 707.5))  # 35
		steep += 35
	steep = 0
	for i in range(SecondPlayer.health):
		screen.blit(hp, (1095 + steep, 707.5))  # 35
		steep += 35
	steep = 0
	# отображение перезарядки
	if FirstPlayer.count_patron == 0:
		screen.blit(patron_ready_player, (350, 710))
	elif reload // 60 < 5:
		screen.blit(per, (340, 710))
	elif reload // 60 == 5:
		screen.blit(ready_player, (370, 710))
	count1 = font.render(str(reload // 60), True, (255, 255, 255))
	screen.blit(count1, (400, 780))

	if FirstPlayer.count_patron == 0:
		screen.blit(patron_ready_player_enemy, (950, 710))
	elif reload_enemy // 60 < 5:
		screen.blit(per, (940, 710))
	elif reload_enemy // 60 == 5:
		screen.blit(ready_player_enemy, (970, 710))
	count2 = font.render(str(reload_enemy // 60), True, (255, 255, 255))
	screen.blit(count2, (990, 780))

	for i in range(FirstPlayer.count_patron // 2):
		screen.blit(snarad, (128 + steep, 780))  # 30
		steep += 30
	steep = 0
	for i in range(SecondPlayer.count_patron // 2):
		screen.blit(snarad, (1090 + steep, 780))  # 30
		steep += 30
	screen.blit(tank_first_player_top, (30, 720))
	screen.blit(tank_second_player_top, (1305, 720))

	# отрисовка счёта
	score = font_score.render(f"{str(score_player)} : {str(score_player_enemy)}", True, (255, 255, 255))
	screen.blit(score, (650, 10))

	pygame.display.flip()

pygame.quit()

# подсчёт очков
with open("score.txt", '+a', encoding = 'utf-8') as file:
	file.write(
		f"[{ctime()}] -> {score_player}:{score_player_enemy} (FirstPlayer:SecondPlayer)\n"
	)
