
"""
main game module
"""
from exceptions import GameOver, EnemyDown
from models import Enemy, Player, Inputs
from settings import LIVES, ENEMY_DOWN_SCORE, GOODBYE_STRING, \
    ENEMY_DOWN_STRING, LIVES_STRING, SCORE_FILE


def play():
    """
    - Entering the player's name
    - Creating a player object - level = 1
    - Creating an enemy object
    - calls the attack and defense
      methods of the player object in an endless loop
    - when an exception occurs, EnemyDown raises the game level,
      creates a new Enemy object with a new level,
      adds +5 points to the player."""
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
            with open(SCORE_FILE, "r") as score_file:
                scores_string = score_file.readlines()
                scores = {}
                for i in scores_string:
                    i = i.strip().split(': ')
                    scores[i[0]] = int(i[1])

            if player.name not in scores:
                with open(SCORE_FILE, "a") as score_file:
                    # write score to scores file
                    score_file.write(f'{player.name}: {player.score}\n')
            elif scores[player.name] < player.score:
                with open(SCORE_FILE, "w") as score_file:
                    scores[player.name] = player.score
                    for key, value in scores.items():
                        score_file.write(f'{key}: {value}\n')

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
