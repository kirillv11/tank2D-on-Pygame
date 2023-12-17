from pygame import Rect
from config import Settings


def create_map():
  img_rect = []
  img = []
  img_rect_grass = []
  img_grass = []
  with open(f"resources/maps/map{Settings.number_map}.txt", "r+", encoding="utf-8") as file:
    w, h = 0, 0
    for line in file:
      for i in line:
        if i != "\n" and len(img_rect) < 200:
          if i == '#':
            wall_rect = Rect(w, h, 50, 50)
            img_rect.append(wall_rect)
            img.append("wall")
          elif i == '/':
            grass_rect = Rect(w, h, 50, 50)
            img_rect_grass.append(grass_rect)
            img_grass.append("grass")
          elif i == '+':
            box_rect = Rect(w, h, 50, 50)
            img_rect.append(box_rect)
            img.append("box")
          elif i == '~':
            water_rect = Rect(w, h, 50, 50)
            img_rect.append(water_rect)
            img.append("water")
        w += 50
      w = 0
      h += 50
    file.close()
    return img_rect, img, img_rect_grass, img_grass
