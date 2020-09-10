from exceptions import GameOver, EnemyDown
from models import Enemy, Player, Inputs

from settings import LIVES, V_SCORE, GOODBYE_STRING


def play():
    """
    - Ввод имени игрока
    - Создание объекта player
    - level = 1
    - Создание объекта enemy
    - в бесконечном цикле вызывает методы attack и defense объекта player
    - при возникновении исключения EnemyDown повышает уровень игры, создает новый объект Enemy с
    новым уровнем, добавляет игроку +5 очков."""
    level = 1
    player = Player(Inputs.input_player_name(), LIVES)
    Inputs.input_start()
    enemy = Enemy(level)

    while True:
        try:
            player.attack(enemy)
        except EnemyDown:
            level += 1
            enemy = Enemy(level)
            player.score += V_SCORE
            continue
        player.defence(enemy)


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        pass

    except KeyboardInterrupt:
        print(GOODBYE_STRING)
        raise
    finally:
        print(GOODBYE_STRING)
    pass
