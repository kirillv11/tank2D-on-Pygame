import pygame
from time import ctime
from map import create_map, img_grass, img_rect_grass, num_of_map


class Player:
    def __init__(self, x_direction, y_direction, speed, speed_shot):
        self.x = x_direction
        self.y = y_direction
        self.speed = speed
        self.patron = []
        self.img_patron = pygame.image.load("img\\other\\patron\\patron.png")
        self.speed_shot = speed_shot

    def up(self):  # движение вверх
        if self.y > 0:
            self.y -= self.speed

    def down(self):  # движение вниз
        if self.y < 620:
            self.y += self.speed

    def right(self):  # движение вправо
        if self.x < 1320:
            self.x += self.speed

    def left(self):  # движение влево
        if self.x > 0:
            self.x -= self.speed

    def draw(self, adress):
        """
            функция отвечает за отрисовку игроков
        """
        adress.set_colorkey((255, 255, 255))
        screen.blit(adress, (self.x, self.y))

    def shot(self, direction, typing):
        """
            функция отвечает за патроны
        """
        if typing == 1:
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
        elif typing == 2:
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

    def shot_speed_shot_and_draw(self, types):
        if types == 1:
            for i in self.patron:
                if collision_second.colliderect(i[0]):
                    self.patron.pop(self.patron.index(i))
                if i[1] == "right":
                    if i[0].x < 1382:
                        i[0].x += self.speed_shot
                    else:
                        self.patron.pop(self.patron.index(i))
                if i[1] == "left":
                    if i[0].x > 0:
                        i[0].x -= self.speed_shot
                    else:
                        self.patron.pop(self.patron.index(i))
                if i[1] == "up":
                    if i[0].y > 0:
                        i[0].y -= self.speed_shot
                    else:
                        self.patron.pop(self.patron.index(i))
                if i[1] == "down":
                    if i[0].y < 682:
                        i[0].y += self.speed_shot
                    else:
                        self.patron.pop(self.patron.index(i))
                for j in img_rect:
                    if j.colliderect(i[0]):
                        self.patron.pop(self.patron.index(i))

                screen.blit(self.img_patron, i[0])
        elif types == 2:
            for i in self.patron:
                if collision_first.colliderect(i[0]):
                    self.patron.pop(self.patron.index(i))
                if i[1] == "right":
                    if i[0].x < 1382:
                        i[0].x += self.speed_shot
                    else:
                        self.patron.pop(self.patron.index(i))
                if i[1] == "left":
                    if i[0].x > 0:
                        i[0].x -= self.speed_shot
                    else:
                        self.patron.pop(self.patron.index(i))
                if i[1] == "up":
                    if i[0].y > 0:
                        i[0].y -= self.speed_shot
                    else:
                        self.patron.pop(self.patron.index(i))
                if i[1] == "down":
                    if i[0].y < 682:
                        i[0].y += self.speed_shot
                    else:
                        self.patron.pop(self.patron.index(i))
                for j in img_rect:
                    if j.colliderect(i[0]):
                        self.patron.pop(self.patron.index(i))

                screen.blit(self.img_patron, i[0])


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
x, y = 0, 0
x_enemy, y_enemy = 1300, 600
go, go_enemy = 0, 0
player_hp, player_enemy_hp = 5, 5
count_player_patron = 12
count_player_enemy_patron = 12
position = "right"
position_enemy = "left"

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
pygame.mixer.music.play(loops=-1)

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

match num_of_map:
    case '1':
        pygame.mixer.music.load("snd\\Map1_battle.mp3")
        pygame.mixer.music.set_volume(volumee)
        pygame.mixer.music.play(loops = -1)
        map_fill = pygame.image.load("img\\texture\\As.jpg")
    case '2':
        pygame.mixer.music.load("snd\\Map2_battle.mp3")
        pygame.mixer.music.set_volume(volumee)
        pygame.mixer.music.play(loops=-1)
        map_fill = pygame.image.load("img\\texture\\Grass.jpg")
    case '3':
        pygame.mixer.music.load("snd\\Map3_battle.mp3")
        pygame.mixer.music.set_volume(volumee)
        pygame.mixer.music.play(loops=-1)
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
player = Player(x, y, speed=2, speed_shot=14)
player_enemy = Player(x_enemy, y_enemy, speed=2, speed_shot=14)

# создание коллизии
collision_first = pygame.Rect(player.x, player.y, tank_first_player_right.get_width(),
                              tank_second_player_right.get_height())
collision_second = pygame.Rect(player_enemy.x, player_enemy.y, tank_second_player_right.get_width(),
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


def conflict(direction, types):
    """
        функции проверяющяя столкновения
    """
    flag = False
    if types == 1:
        if direction == 'up':
            line_x, line_y = player.x + 32, player.y
            line_x_right, line_y_right = player.x + 60, player.y
            line_x_left, line_y_left = player.x, player.y

            line_y_before = player.y
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
                player.up()
        elif direction == 'down':
            line_x, line_y = player.x + 32, player.y + 75
            line_x_right, line_y_right = player.x + 64, player.y + 75
            line_x_left, line_y_left = player.x, player.y + 75

            line_y_before = player.y + 75
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
                player.down()
        elif direction == 'right':
            line_x, line_y = player.x + 80, player.y + 32
            line_x_right, line_y_right = player.x + 80, player.y
            line_x_left, line_y_left = player.x + 80, player.y + 60

            line_x_before = player.x + 26
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
                player.right()
        elif direction == 'left':
            line_x, line_y = player.x - 12, player.y + 32
            line_x_right, line_y_right = player.x - 12, player.y
            line_x_left, line_y_left = player.x - 12, player.y + 60

            line_x_before = player.x - 12
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
                player.left()
                for i in img_rect:
                    if collision_first.colliderect(i):
                        player.x -= 0.01
                        break
    elif types == 2:
        if direction == 'up':
            line_x, line_y = player_enemy.x + 38, player_enemy.y
            line_x_right, line_y_right = player_enemy.x + 80, player_enemy.y
            line_x_left, line_y_left = player_enemy.x, player_enemy.y

            line_y_before = player_enemy.y
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
                player_enemy.up()

        elif direction == 'down':
            line_x, line_y = player_enemy.x + 38, player_enemy.y + 100
            line_x_right, line_y_right = player_enemy.x + 79, player_enemy.y + 100
            line_x_left, line_y_left = player_enemy.x, player_enemy.y + 100

            line_y_before = player_enemy.y + 100
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
                player_enemy.down()
        elif direction == 'right':
            line_x, line_y = player_enemy.x + 100, player_enemy.y + 38
            line_x_right, line_y_right = player_enemy.x + 100, player_enemy.y + 79
            line_x_left, line_y_left = player_enemy.x + 100, player_enemy.y

            line_x_before = player_enemy.x + 100
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
                player_enemy.right()
        elif direction == 'left':
            line_x, line_y = player_enemy.x + 15, player_enemy.y + 38
            line_x_right, line_y_right = player_enemy.x + 15, player_enemy.y + 79
            line_x_left, line_y_left = player_enemy.x + 15, player_enemy.y

            line_x_before = player_enemy.x + 15
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
                player_enemy.left()


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
                if count_player_patron > 0 and reload == 300:
                    player.shot(position, 1)
                    count_player_patron -= 1
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
                if count_player_enemy_patron > 0 and reload_enemy == 300:
                    player_enemy.shot(position_enemy, 2)
                    count_player_enemy_patron -= 1
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

    screen.blit(map_fill, (0, 0))  # заливка экрана

    pygame.draw.rect(screen, [80, 80, 80], [0, 700, width, 150])
    # движение объектов
    if move_up and go == 1:
        position = "up"
        conflict('up', 1)
    elif move_down and go == 1:
        position = "down"
        conflict('down', 1)
    elif move_right and go == 1:
        position = "right"
        conflict('right', 1)
    elif move_left and go == 1:
        position = "left"
        conflict('left', 1)

    # игрок на место возвращается после взрыва
    if player_hp <= 0:
        player.x, player.y = 0, 0
        player_hp = 5
        count_player_patron = 12
        score_player_enemy += 1
    if player_enemy_hp <= 0:
        player_enemy.x, player_enemy.y = 1300, 600
        player_enemy_hp = 5
        count_player_enemy_patron = 12
        score_player += 1

    # отрисовка объекта
    if position == 'up':
        player.draw(tank_first_player_top)
        collision_first = pygame.Rect(player.x, player.y, tank_first_player_top.get_width(),
                                      tank_second_player_top.get_height())
    elif position == 'down':
        player.draw(tank_first_player_bottom)
        collision_first = pygame.Rect(player.x, player.y, tank_first_player_bottom.get_width(),
                                      tank_second_player_bottom.get_height())
    elif position == 'right':
        player.draw(tank_first_player_right)
        collision_first = pygame.Rect(player.x, player.y, tank_first_player_right.get_width(),
                                      tank_second_player_right.get_height())
    elif position == "left":
        player.draw(tank_first_player_left)
        collision_first = pygame.Rect(player.x, player.y, tank_first_player_left.get_width(),
                                      tank_second_player_left.get_height())

    # движение объектов
    if move_up_enemy and go_enemy == 1:
        position_enemy = "up"
        conflict('up', 2)
    elif move_down_enemy and go_enemy == 1:
        position_enemy = "down"
        conflict('down', 2)
    elif move_right_enemy and go_enemy == 1:
        position_enemy = "right"
        conflict('right', 2)
    elif move_left_enemy and go_enemy == 1:
        position_enemy = "left"
        conflict('left', 2)

    # отрисовка объекта
    if position_enemy == 'up':
        player_enemy.draw(tank_second_player_top)
        collision_second = pygame.Rect(player_enemy.x, player_enemy.y, tank_second_player_top.get_width(),
                                       tank_second_player_top.get_height())
    elif position_enemy == 'down':
        player_enemy.draw(tank_second_player_bottom)
        collision_second = pygame.Rect(player_enemy.x, player_enemy.y, tank_second_player_bottom.get_width(),
                                       tank_second_player_bottom.get_height())
    elif position_enemy == 'right':
        player_enemy.draw(tank_second_player_right)
        collision_second = pygame.Rect(player_enemy.x, player_enemy.y, tank_second_player_right.get_width(),
                                       tank_second_player_right.get_height())
    elif position_enemy == "left":
        player_enemy.draw(tank_second_player_left)
        collision_second = pygame.Rect(player_enemy.x, player_enemy.y, tank_second_player_left.get_width(),
                                       tank_second_player_left.get_height())

    # вызывание функции из классов
    player.shot_speed_shot_and_draw(1)
    player_enemy.shot_speed_shot_and_draw(2)

    # рисование карты
    for i in img_rect:
        if img[img_rect.index(i)] == "box":
            screen.blit(box, i)
        elif img[img_rect.index(i)] == "wall":
            screen.blit(wall, i)
        elif img[img_rect.index(i)] == "water":
            screen.blit(water, i)

    # отрисовка травы
    for i in img_rect_grass:
        if img_grass[img_rect_grass.index(i)] == "grass":
            screen.blit(grass, i)

    # отрисовка нижней части
    info.set_colorkey((255, 255, 255))
    hp.set_colorkey((255, 255, 255))
    screen.blit(info, (0, 700))

    # проверка на столкновение
    for i in player_enemy.patron:
        if collision_first.colliderect(i[0]):
            if player_hp > 0:
                player_hp -= 1
                probitie.play()
            elif player_hp == 1:
                player_hp -= 1
                destruction.play()

    # проверка на столкновение
    for i in player.patron:
        if collision_second.colliderect(i[0]):
            if player_enemy_hp > 1:
                player_enemy_hp -= 1
                probitie.play()
            elif player_enemy_hp == 1:
                player_enemy_hp -= 1
                destruction.play()

    # отображение элементов нижней панели
    steep = 0
    for i in range(player_hp):
        screen.blit(hp, (130 + steep, 707.5))  # 35
        steep += 35
    steep = 0
    # отображение перезарядки
    if count_player_patron == 0:
        screen.blit(patron_ready_player, (350, 710))
    elif reload // 60 < 5:
        screen.blit(per, (340, 710))
    elif reload // 60 == 5:
        screen.blit(ready_player, (370, 710))

    count1 = font.render(str(reload // 60), True, (255, 255, 255))
    screen.blit(count1, (400, 780))
    for i in range(player_enemy_hp):
        screen.blit(hp, (1095 + steep, 707.5))  # 35
        steep += 35
    steep = 0
    # отображение перезарядки
    if count_player_patron == 0:
        screen.blit(patron_ready_player_enemy, (950, 710))
    elif reload_enemy // 60 < 5:
        screen.blit(per, (940, 710))
    elif reload_enemy // 60 == 5:
        screen.blit(ready_player_enemy, (970, 710))
    count2 = font.render(str(reload_enemy // 60), True, (255, 255, 255))
    screen.blit(count2, (990, 780))
    for i in range(count_player_patron // 2):
        screen.blit(snarad, (128 + steep, 780))  # 30
        steep += 30
    steep = 0
    for i in range(count_player_enemy_patron // 2):
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

