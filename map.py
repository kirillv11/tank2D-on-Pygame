import pygame
from random import randint

img_rect = []
img = []
img_rect_grass = []
img_grass = []
map_spicok = ["1", "2", "3", "1", "2", "3", "1", "2", "3"]  # здесь все карты
map_random = map_spicok[randint(0, 8)]
def create_map():
    with open("map" + map_random + ".txt", "r+", encoding="utf-8") as file:
        w, h = 0, 0
        for line in file:
            for i in range(len(line)):
                if line[i] != "\n" and len(img_rect) < 200:
                    if line[i] == "#":
                        wall_rect = pygame.Rect(w, h, 50, 50)
                        img_rect.append(wall_rect)
                        img.append("wall")
                    elif line[i] == "/":
                        grass_rect = pygame.Rect(w, h, 50, 50)
                        img_rect_grass.append(grass_rect)
                        img_grass.append("grass")
                    elif line[i] == "+":
                        box_rect = pygame.Rect(w, h, 50, 50)
                        img_rect.append(box_rect)
                        img.append("box")
                    elif line[i] == "~":
                        water_rect = pygame.Rect(w, h, 50, 50)
                        img_rect.append(water_rect)
                        img.append("water")

                w += 50

            w = 0
            h += 50
        file.close()
        return img_rect, img, map_random
