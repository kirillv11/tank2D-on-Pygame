import pygame

pygame.init()
from config import Settings
from map import create_map
from load_texture import *
from load_font import *
from collisions import collision
from player import Player
from functions import record_points, draw_score


def main():
  screen = pygame.display.set_mode((Settings.width, Settings.height))
  clock = pygame.time.Clock()

  def menu():
    screen.blit(logo, (0, 0))
    pygame.display.flip()
    print("Write a number of your tank (1 - 4)")
    technic_first_player = input("1 player: ")
    technic_second_player = input("2 player: ")
    if not technic_second_player in [1, 2, 3, 4] or not technic_first_player in [1, 2, 3, 4]:
      technic_first_player = 1
      technic_second_player = 1
    else:
      technic_first_player = int(technic_first_player)
      technic_second_player = int(technic_second_player)
    return technic_first_player, technic_second_player

  img_rect, img, img_rect_grass, img_grass = create_map()

  first_player_type_tank, second_player_type_tank = menu()  # отрисовка меню

  # инициализация классов
  FirstPlayer = Player(
    0, 0, 'right', Settings.speed, 5, 14, 12, first_player_type_tank
  )
  SecondPlayer = Player(
    1300, 600, 'left', Settings.speed, 5, 14, 12, second_player_type_tank
  )

  # settings
  go, go_enemy = 0, 0

  # здесь номер карты
  pygame.mixer.init()

  # настройка музыки
  volume = 0.5
  pygame.mixer.music.load("resources/sounds/intro.mp3")
  pygame.mixer.music.set_volume(volume)
  pygame.mixer.music.play(loops=-1)

  volume = 0.7

  if Settings.number_map == 1:
    pygame.mixer.music.load("resources/sounds/Map1_battle.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=-1)
    map_fill = pygame.image.load("resources/image/texture/concrete.jpg")
  if Settings.number_map == 2:
    pygame.mixer.music.load("resources/sounds/Map2_battle.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=-1)
    map_fill = pygame.image.load("resources/image/texture/grass.jpg")
  if Settings.number_map == 3:
    pygame.mixer.music.load("resources/sounds/Map3_battle.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=-1)
    map_fill = pygame.image.load("resources/image/texture/grass.jpg")

  destruction = pygame.mixer.Sound("resources/sounds/Probitie.mp3")
  shot = pygame.mixer.Sound("resources/sounds/f4ee46bb060c102.mp3")
  is_breaking = pygame.mixer.Sound("resources/sounds/1.mp3")
  shot.set_volume(volume)
  destruction.set_volume(volume)
  is_breaking.set_volume(volume)

  pygame.mixer.Channel(0).play(pygame.mixer.Sound("resources/sounds/zvuk-zavedennogo-tanka-motora-12255.mp3"))
  pygame.mixer.Channel(0).set_volume(0.15)

  move_up, move_down, move_right, move_left = False, False, False, False
  move_up_enemy, move_down_enemy, move_right_enemy, move_left_enemy = False, False, False, False

  # объекты карты
  img_rect = create_map()[0]
  img = create_map()[1]

  # перезарядка
  count1 = main_font.render(str(FirstPlayer.reload), True, (255, 255, 255))
  count2 = main_font.render(str(SecondPlayer.reload), True, (255, 255, 255))
  running = True
  while running:
    clock.tick(Settings.FPS)

    # настройка перезарядки
    if FirstPlayer.reload != 300:
      FirstPlayer.reload += 1
    if SecondPlayer.reload != 300:
      SecondPlayer.reload += 1

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
          if FirstPlayer.count_patron > 0 and FirstPlayer.reload == 300:
            FirstPlayer.shot(FirstPlayer.direction, 1)
            FirstPlayer.count_patron -= 1
            FirstPlayer.reload = 0
            shot.play()
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
          if SecondPlayer.count_patron > 0 and SecondPlayer.reload == 300:
            SecondPlayer.shot(SecondPlayer.direction, 2)
            SecondPlayer.count_patron -= 1
            SecondPlayer.reload = 0
            shot.play()
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
    pygame.draw.rect(screen, [80, 80, 80], [0, 700, Settings.width, 150])

    # движение объектов
    if move_up and go == 1:
      FirstPlayer.direction = 'up'
      collision('up', 1, FirstPlayer, SecondPlayer, img_rect)
    elif move_down and go == 1:
      FirstPlayer.direction = 'down'
      collision('down', 1, FirstPlayer, SecondPlayer, img_rect)
    elif move_right and go == 1:
      FirstPlayer.direction = 'right'
      collision('right', 1, FirstPlayer, SecondPlayer, img_rect)
    elif move_left and go == 1:
      FirstPlayer.direction = 'left'
      collision('left', 1, FirstPlayer, SecondPlayer, img_rect)

    # rebirth
    if FirstPlayer.health <= 0:
      FirstPlayer.x, FirstPlayer.y = 0, 0
      FirstPlayer.health = 5
      FirstPlayer.count_patron = 12
      SecondPlayer.score += 1
    if SecondPlayer.health <= 0:
      SecondPlayer.x, SecondPlayer.y = 1300, 600
      SecondPlayer.health = 5
      SecondPlayer.count_patron = 12
      FirstPlayer.score += 1

    # drawing object
    FirstPlayer.draw(screen)

    # движение объектов
    if move_up_enemy and go_enemy == 1:
      SecondPlayer.direction = 'up'
      collision('up', 2, FirstPlayer, SecondPlayer, img_rect)
    elif move_down_enemy and go_enemy == 1:
      SecondPlayer.direction = 'down'
      collision('down', 2, FirstPlayer, SecondPlayer, img_rect)
    elif move_right_enemy and go_enemy == 1:
      SecondPlayer.direction = 'right'
      collision('right', 2, FirstPlayer, SecondPlayer, img_rect)
    elif move_left_enemy and go_enemy == 1:
      SecondPlayer.direction = 'left'
      collision('left', 2, FirstPlayer, SecondPlayer, img_rect)

    # отрисовка объекта
    SecondPlayer.draw(screen)

    # drawing shots
    FirstPlayer.shot_draw(screen, img_rect)
    SecondPlayer.shot_draw(screen, img_rect)
    for obj in SecondPlayer.patron:
      if FirstPlayer.rect_collision.colliderect(obj[0]):
        SecondPlayer.patron.remove(obj)
        FirstPlayer.health -= 1
        if FirstPlayer.health >= 1:
          is_breaking.play()
        else:
          destruction.play()
    for obj in FirstPlayer.patron:
      if SecondPlayer.rect_collision.colliderect(obj[0]):
        FirstPlayer.patron.remove(obj)
        SecondPlayer.health -= 1
        if SecondPlayer.health >= 1:
          is_breaking.play()
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
    health.set_colorkey((255, 255, 255))
    screen.blit(info, (0, 700))

    # отображение элементов нижней панели
    steep = 0
    for i in range(FirstPlayer.health):
      screen.blit(health, (130 + steep, 707.5))  # 35
      steep += 35
    steep = 0
    for i in range(SecondPlayer.health):
      screen.blit(health, (1095 + steep, 707.5))  # 35
      steep += 35
    steep = 0
    # отображение перезарядки
    if FirstPlayer.count_patron == 0:
      screen.blit(patron_ready_player, (350, 710))
    elif FirstPlayer.reload // 60 < 5:
      screen.blit(per, (340, 710))
    elif FirstPlayer.reload // 60 == 5:
      screen.blit(ready_player, (370, 710))
    count1 = main_font.render(str(FirstPlayer.reload // 60), True, (255, 255, 255))
    screen.blit(count1, (400, 780))

    if FirstPlayer.count_patron == 0:
      screen.blit(patron_ready_player_enemy, (950, 710))
    elif SecondPlayer.reload // 60 < 5:
      screen.blit(per, (940, 710))
    elif SecondPlayer.reload // 60 == 5:
      screen.blit(ready_player_enemy, (970, 710))
    count2 = main_font.render(str(SecondPlayer.reload // 60), True, (255, 255, 255))
    screen.blit(count2, (990, 780))

    for i in range(FirstPlayer.count_patron // 2):
      screen.blit(bullet, (128 + steep, 780))  # 30
      steep += 30
    steep = 0
    for i in range(SecondPlayer.count_patron // 2):
      screen.blit(bullet, (1090 + steep, 780))  # 30
      steep += 30
    screen.blit(FirstPlayer.forward, (30, 720))
    screen.blit(SecondPlayer.forward, (1305, 720))
    draw_score(screen, FirstPlayer.score, SecondPlayer.score, font_score)
    pygame.display.flip()

  pygame.quit()
  record_points(FirstPlayer.score, SecondPlayer.score)


if __name__ == "__main__":
  main()
