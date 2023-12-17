from time import ctime


def record_points(first_player_score, second_player_score):
  with open("resources/score.txt", '+a', encoding='utf-8') as file:
    file.write(
      f"[{ctime()}] -> {first_player_score}:{second_player_score} (FirstPlayer:SecondPlayer)\n"
    )


def draw_score(screen, first_player_score, second_player_score, font):
  # отрисовка счёта
  score = font.render(f"{str(first_player_score)} : {str(second_player_score)}", True, (255, 255, 255))
  screen.blit(score, (650, 10))
