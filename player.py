import pygame


class PlayerImage:
  def __init__(self, tank_type: int = 1):
    self.forward = pygame.image.load(
      "resources/image/first_player/Tank-" + str(tank_type) + "_1pl.png"
    )
    # .set_colorkey((255, 255, 255))
    self.bottom = pygame.image.load(
      "resources/image/first_player/Tank-" + str(tank_type) + "_1pl_d.png"
    )
    self.right = pygame.image.load(
      "resources/image/first_player/Tank-" + str(tank_type) + "_1pl_r.png"
    )
    self.left = pygame.image.load(
      "resources/image/first_player/Tank-" + str(tank_type) + "_1pl_l.png"
    )


class Player(PlayerImage):
  def __init__(self, x: int, y: int, direction: str, speed: int, health: int, speed_shot: int, count_patron: int,
               tank_type: int = 1):
    super().__init__(tank_type)
    self.x: int = x
    self.y: int = y
    self.direction: str = direction
    self.count_patron: int = count_patron
    self.health: int = health
    self.speed: int = speed
    self.patron = []
    self.img_patron = pygame.image.load("resources/image/other/patron/patron.png")
    self.speed_shot = speed_shot
    self.score: int = 0
    self.reload: int = 0
    self.rect_collision = pygame.Rect(self.x, self.y, self.right.get_width(), self.right.get_height())

  def go_up(self):  # go up
    if self.y >= 0:
      self.y -= self.speed

  def go_down(self):  # go down
    if self.y < 620:
      self.y += self.speed

  def go_right(self):  # go right
    if self.x < 1320:
      self.x += self.speed

  def go_left(self):  # go left
    if self.x >= 0:
      self.x -= self.speed

  def draw(self, screen):
    """this function is responsible for rendering the player"""
    if self.direction == "up":
      screen.blit(self.forward, (self.x, self.y))
      self.rect_collision = pygame.Rect(self.x, self.y, self.forward.get_width(), self.forward.get_height())
    if self.direction == "right":
      screen.blit(self.right, (self.x, self.y))
      self.rect_collision = pygame.Rect(self.x, self.y, self.right.get_width(), self.right.get_height())
    if self.direction == "left":
      screen.blit(self.left, (self.x, self.y))
      self.rect_collision = pygame.Rect(self.x, self.y, self.left.get_width(), self.left.get_height())
    if self.direction == "down":
      screen.blit(self.bottom, (self.x, self.y))
      self.rect_collision = pygame.Rect(self.x, self.y, self.bottom.get_width(), self.bottom.get_height())

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

  def shot_draw(self, screen, img_rect):
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
