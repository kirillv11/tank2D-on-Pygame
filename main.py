import pygame

pygame.init()

from config import *
from map import create_map
from load_texture import *
from load_font import *
from collisions import collision
from player import Player
from functions import record_points, draw_score, menu


def setting_music():
    if Settings.number_map == 1:
        pygame.mixer.music.load("resources/sounds/Map1_battle.mp3")
        map_fill = pygame.image.load("resources/image/texture/concrete.jpg")
    if Settings.number_map == 2:
        pygame.mixer.music.load("resources/sounds/Map2_battle.mp3")
        map_fill = pygame.image.load("resources/image/texture/grass.jpg")
    if Settings.number_map == 3:
        pygame.mixer.music.load("resources/sounds/Map3_battle.mp3")
        map_fill = pygame.image.load("resources/image/texture/grass.jpg")

    pygame.mixer.music.set_volume(Settings.volume)
    pygame.mixer.music.play(loops=-1)

    destruction = pygame.mixer.Sound("resources/sounds/Probitie.mp3")
    shot = pygame.mixer.Sound("resources/sounds/shot.mp3")
    is_breaking = pygame.mixer.Sound("resources/sounds/1.mp3")
    shot.set_volume(Settings.volume)
    destruction.set_volume(Settings.volume)
    is_breaking.set_volume(Settings.volume)

    pygame.mixer.Channel(0).play(pygame.mixer.Sound("resources/sounds/motor.mp3"))
    pygame.mixer.Channel(0).set_volume(0.15)
    return map_fill, destruction, shot, is_breaking


def main():
    screen = pygame.display.set_mode((Settings.width, Settings.height))
    clock = pygame.time.Clock()

    img_rect, img, img_rect_grass, img_grass = create_map()
    first_player_type_tank, second_player_type_tank = menu(screen, logo)

    # инициализация классов
    FirstPlayer = Player(
        0, 0, 'right', Settings.speed, 5, 14, 12, first_player_type_tank
    )
    SecondPlayer = Player(
        1300, 600, 'left', Settings.speed, 5, 14, 12, second_player_type_tank
    )

    # settings
    go, go_enemy = 0, 0

    pygame.mixer.init()
    map_fill, destruction, shot, is_breaking = setting_music()

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
                    FirstPlayer.move['up'] = 1
                    go += 1
                if event.key == pygame.K_s:
                    FirstPlayer.move['down'] = 1
                    go += 1
                if event.key == pygame.K_d:
                    FirstPlayer.move['right'] = 1
                    go += 1
                if event.key == pygame.K_a:
                    FirstPlayer.move['left'] = 1
                    go += 1
                if event.key == pygame.K_SPACE:  # стрельба
                    if FirstPlayer.count_patron > 0 and FirstPlayer.reload == 300:
                        FirstPlayer.shot(FirstPlayer.direction, 1)
                        FirstPlayer.count_patron -= 1
                        FirstPlayer.reload = 0
                        shot.play()
                if event.key == pygame.K_UP:
                    SecondPlayer.move['up'] = 1
                    go_enemy += 1
                if event.key == pygame.K_DOWN:
                    SecondPlayer.move['down'] = 1
                    go_enemy += 1
                if event.key == pygame.K_RIGHT:
                    SecondPlayer.move['right'] = 1
                    go_enemy += 1
                if event.key == pygame.K_LEFT:
                    SecondPlayer.move['left'] = 1
                    go_enemy += 1
                if event.key == pygame.K_p:  # пауза
                    pygame.mixer.music.pause()
                if event.key == pygame.K_o:  # продолжение проигрывания
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_PAGEUP:  # регулировка громкости(громче)
                    Settings.volume += 0.1
                    shot.set_volume(Settings.volume)
                    pygame.mixer.music.set_volume(Settings.volume)
                if event.key == pygame.K_PAGEDOWN:  # регулировка громкости(тише)
                    Settings.volume -= 0.1
                    shot.set_volume(Settings.volume)
                    pygame.mixer.music.set_volume(Settings.volume)

            if event.type == pygame.MOUSEBUTTONDOWN:  # стрельба
                if event.button == 1:
                    if SecondPlayer.count_patron > 0 and SecondPlayer.reload == 300:
                        SecondPlayer.shot(SecondPlayer.direction, 2)
                        SecondPlayer.count_patron -= 1
                        SecondPlayer.reload = 0
                        shot.play()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    FirstPlayer.move['up'] = 0
                    go -= 1
                if event.key == pygame.K_s:
                    FirstPlayer.move['down'] = 0
                    go -= 1
                if event.key == pygame.K_d:
                    FirstPlayer.move['right'] = 0
                    go -= 1
                if event.key == pygame.K_a:
                    FirstPlayer.move['left'] = 0
                    go -= 1

                if event.key == pygame.K_UP:
                    SecondPlayer.move['up'] = 0
                    go_enemy -= 1
                if event.key == pygame.K_DOWN:
                    SecondPlayer.move['down'] = 0
                    go_enemy -= 1
                if event.key == pygame.K_RIGHT:
                    SecondPlayer.move['right'] = 0
                    go_enemy -= 1
                if event.key == pygame.K_LEFT:
                    SecondPlayer.move['left'] = 0
                    go_enemy -= 1

        screen.blit(map_fill, (0, 0))
        pygame.draw.rect(screen, [80, 80, 80], [0, 700, Settings.width, 150])

        # движение объектов
        if FirstPlayer.move['up'] and go == 1:
            FirstPlayer.direction = 'up'
            collision(FirstPlayer.direction, 1, FirstPlayer, SecondPlayer, img_rect)
        elif FirstPlayer.move['down'] and go == 1:
            FirstPlayer.direction = 'down'
            collision(FirstPlayer.direction, 1, FirstPlayer, SecondPlayer, img_rect)
        elif FirstPlayer.move['right'] and go == 1:
            FirstPlayer.direction = 'right'
            collision(FirstPlayer.direction, 1, FirstPlayer, SecondPlayer, img_rect)
        elif FirstPlayer.move['left'] and go == 1:
            FirstPlayer.direction = 'left'
            collision(FirstPlayer.direction, 1, FirstPlayer, SecondPlayer, img_rect)

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
        if SecondPlayer.move['up'] and go_enemy == 1:
            SecondPlayer.direction = 'up'
            collision('up', 2, FirstPlayer, SecondPlayer, img_rect)
        elif SecondPlayer.move['down'] and go_enemy == 1:
            SecondPlayer.direction = 'down'
            collision('down', 2, FirstPlayer, SecondPlayer, img_rect)
        elif SecondPlayer.move['right'] and go_enemy == 1:
            SecondPlayer.direction = 'right'
            collision('right', 2, FirstPlayer, SecondPlayer, img_rect)
        elif SecondPlayer.move['left'] and go_enemy == 1:
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

        steep = 0
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
