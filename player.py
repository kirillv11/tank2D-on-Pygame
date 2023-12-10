import pygame


class Player:
  def __init__(self, x_direction, y_direction, direction, speed, health, speed_shot, count_patron, screen, img_rect):
    self.x = x_direction
    self.y = y_direction
    self.direction = direction
    self.count_patron = count_patron
    self.health = health
    self.speed = speed
    self.patron = []
    self.img_patron = pygame.image.load("resources/image/other/patron/patron.png")
    self.speed_shot = speed_shot
    self.score: int = 0
    self.screen = screen
    self.img_rect = img_rect
    self.reload = 0

  def up(self):  # go up
    if self.y >= 0:
      self.y -= self.speed

  def down(self):  # go down
    if self.y < 620:
      self.y += self.speed

  def right(self):  # go right
    if self.x < 1320:
      self.x += self.speed

  def left(self):  # go left
    if self.x >= 0:
      self.x -= self.speed

  def draw(self, adress):
    """this function is responsible for rendering the player"""
    adress.set_colorkey((255, 255, 255))
    self.screen.blit(adress, (self.x, self.y))

  def shot(self, direction, types):
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

  def shot_draw(self):
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
        for rect in self.img_rect:
          if rect.colliderect(patron_object[0]):
            del_flag = True

      if del_flag:
        self.patron.remove(patron_object)
      else:
        self.screen.blit(self.img_patron, patron_object[0])
