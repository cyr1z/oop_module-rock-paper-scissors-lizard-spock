from exceptions import GameOver, EnemyDown
from models import Enemy, Player, Inputs
from settings import LIVES, ENEMY_DOWN_SCORE, GOODBYE_STRING, ENEMY_DOWN_STRING, LIVES_STRING, SCORE_FILE


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
            player.defence(enemy)
        except EnemyDown:
            level += 1
            enemy = Enemy(level)
            player.score += ENEMY_DOWN_SCORE
            print(ENEMY_DOWN_STRING, player.score)
            print(LIVES_STRING, player.lives)
            continue
        except GameOver:
            with open(SCORE_FILE, "a") as score_file:
                score_file.write(f'{player.name}: {player.score}\n')
                raise GameOver


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        pass

    except KeyboardInterrupt:
        pass
    finally:
        print(GOODBYE_STRING)
    pass
