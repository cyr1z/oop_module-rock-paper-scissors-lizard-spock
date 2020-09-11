from settings import SCORE_FILE


class GameOver(Exception):
    def __init__(self, player=0):
        self.player = player
        from models import Player
        if isinstance(self.player, Player):
            # print(f'{self.player.name}: {self.player.score}\n')
            with open(SCORE_FILE, "a") as f:
                f.write(f'{self.player.name}: {self.player.score}\n')
    pass


class EnemyDown(Exception):
    pass
