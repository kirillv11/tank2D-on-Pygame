from pygame import font
from config import Settings

main_font = font.SysFont('Consolas', 20)

per = main_font.render('Перезарядка', True, (255, 255, 255))
ready_player = main_font.render('Готово', True, (255, 255, 255))
ready_player_enemy = main_font.render('Готово', True, (255, 255, 255))
patron_ready_player = main_font.render('нет патрон', True, (255, 255, 255))
patron_ready_player_enemy = main_font.render('нет патрон', True, (255, 255, 255))

font_score = font.SysFont('Consolas', 40)
# score = font_score.render(f"{str(Settings.FirstPlayer.score)} : {str(Settings.SecondPlayer.score)}", True, (255, 255, 255))
score = font_score.render("0 : 0", True, (255, 255, 255))
