import pygame
from config import Settings


def collision(direction, types, FirstPlayer, SecondPlayer, collision_first, collision_second, img_rect):
  """
    Функция, проверяющая столкновения
  """
  flag = False
  if types == 1:
    if direction == 'up':
      line_x, line_y = FirstPlayer.x + 32, FirstPlayer.y
      line_x_right, line_y_right = FirstPlayer.x + 60, FirstPlayer.y
      line_x_left, line_y_left = FirstPlayer.x, FirstPlayer.y

      for _ in range(100):
        if line_y_left < 0 or flag:
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
      if abs(int(FirstPlayer.y - line_y_right)) > 5:
        FirstPlayer.up()
    elif direction == 'down':
      line_x, line_y = FirstPlayer.x + 32, FirstPlayer.y + 75
      line_x_right, line_y_right = FirstPlayer.x + 64, FirstPlayer.y + 75
      line_x_left, line_y_left = FirstPlayer.x, FirstPlayer.y + 75

      line_y_before = FirstPlayer.y + 75
      s = []
      for _ in range(100):
        if line_y > 700 or flag:
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
      for _ in range(100):
        if line_x > 1400 or flag:
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
      for _ in range(100):
        if line_x < 0 or flag:
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
        int(line_x_before - line_x_left)
      ) > 1:
        FirstPlayer.left()
        for rect in img_rect:
          if collision_first.colliderect(rect):
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
      for _ in range(100):
        if line_x > 1400 or flag:
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
      for _ in range(100):
        if line_x < 0 or flag:
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
