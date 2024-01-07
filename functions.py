from time import ctime
from pygame import display


def record_points(first_player_score, second_player_score):
    with open("resources/score.txt", '+a', encoding='utf-8') as file:
        file.write(
            f"[{ctime()}] -> {first_player_score}:{second_player_score} (FirstPlayer:SecondPlayer)\n"
        )


def draw_score(screen, first_player_score, second_player_score, font):
    # отрисовка счёта
    score = font.render(f"{str(first_player_score)} : {str(second_player_score)}", True, (255, 255, 255))
    screen.blit(score, (650, 10))


def menu(screen, logo):
    screen.blit(logo, (0, 0))
    display.flip()
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
