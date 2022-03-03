import pygame
import random

img_rect = []
img = []
img_rect_2 = []
img_2 = []
map_spicok = ["2", "3", "1", "2", "3", "1", "2", "3", "1"]  # здесь все карты
map_random = map_spicok[random.randint(0, 8)]  # выбираем карту
def create_map():
    with open("map" + map_random + ".txt", "r+", encoding="utf-8") as file:
        h = 0
        w = 0
        for line in file:
            for i in range(len(line)):
                if line[i] != "\n":
                    if line[i] == "#":
                        wall_rect = pygame.Rect(w, h, 50, 50)
                        if len(img_rect) < 200:
                            img_rect.append(wall_rect)
                            img.append("wall")
                    elif line[i] == "/":
                        grass_rect = pygame.Rect(w, h, 50, 50)
                        if len(img_rect) < 200:
                            pass
                            img_rect_2.append(grass_rect)
                            img_2.append("grass")
                    elif line[i] == "+":
                        box_rect = pygame.Rect(w, h, 50, 50)
                        if len(img_rect) < 200:
                            img_rect.append(box_rect)
                            img.append("box")
                    elif line[i] == "~":
                        water_rect = pygame.Rect(w, h, 50, 50)
                        if len(img_rect) < 200:
                            img_rect.append(water_rect)
                            img.append("water")

                w += 50

            w = 0
            h += 50

        return img_rect, img, map_random




