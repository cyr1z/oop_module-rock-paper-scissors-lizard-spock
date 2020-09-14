"""
main game module
"""
from exceptions import GameOver, EnemyDown
from models import Enemy, Player, Inputs, Scores
from color import cli_color
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
            print(cli_color(f'{ENEMY_DOWN_STRING} {player.score}', 'c'))
            print(LIVES_STRING, player.lives)
            continue

        except GameOver:
            scores = Scores()
            # read scores from file
            try:
                scores.read_from_file(SCORE_FILE)
            except FileNotFoundError:
                pass
            # write score to scores file
            scores.new_result(player, SCORE_FILE)
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
