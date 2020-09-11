from enum import Enum
from random import randint
from exceptions import EnemyDown, GameOver
from settings import WELCOME_STRING, START_STRING, START_EXIT_KEY_WORDS, WRONG_SELECT, SELECT_STRiNG
from settings import ATTACK_STRING, DEFENSE_STRING, GAME_OVER_STRING, LIVES_STRING


class Attacks(Enum):
    robber = 1
    warrior = 2
    wizard = 3


class Enemy:
    """- свойства - level, lives.
    - конструктор принимает уровень. Уровень жизней противнка = уровень противника."""

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """returns a random number between one and three"""
        return randint(1, 3)

    def decrease_lives(self):
        """уменьшает количество жизней. Когда жизней становится 0 вызывает
        исключение EnemyDown."""
        self.lives -= 1
        if not self.lives:
            raise EnemyDown


class Player:
    score = 0
    allowed_attacks = [1, 2, 3]

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
        pass

    @staticmethod
    def fight(attack, defense):

        """- возвращает результат раунда -
        0 если ничья,
        -1 если атака неуспешна,
        1 если атака успешна.
        """
        # draw
        if attack == defense:
            return 0
        # lose
        if attack == 1 and defense == 2 or \
           attack == 2 and defense == 3 or \
           attack == 3 and defense == 1:
            return -1
        # won
        if attack == 2 and defense == 1 or \
           attack == 3 and defense == 2 or \
           attack == 1 and defense == 3:
            return 1

    def decrease_lives(self):
        """- то  же, что и Enemy.decrease_lives(), вызывает исключение
            GameOver."""
        self.lives -= 1
        if not self.lives:
            print(GAME_OVER_STRING, self.score)
            print(LIVES_STRING, self.lives)
            raise GameOver

    def attack(self, enemy_obj):
        """- получает ввод от пользователя(1, 2, 3), выбирает
            атаку противника из объекта enemy_obj;
             вызывает метод fight();
            Если результат боя 0 - вывести "It's a draw!",
            если 1 = "You attacked successfully!" и уменьшает количество жизней противника на 1,
            если - 1 = "You missed!"""
        my_choice = Inputs.select_player_attack()
        result = self.fight(my_choice, enemy_obj.select_attack())
        print(ATTACK_STRING[result])
        if result == 1:
            enemy_obj.decrease_lives()
            self.score += 1

    def defence(self, enemy_obj):
        """- то же самое, что и метод attack(),
        только в метод fight первым передается атака противника,
        и при удачной атаке противника вызывается метод decrease_lives игрока."""
        my_choice = Inputs.select_player_attack()
        result = self.fight(enemy_obj.select_attack(), my_choice)
        print(DEFENSE_STRING[result])
        if result == 1:
            self.decrease_lives()


class Inputs:

    @staticmethod
    def input_player_name(string=WELCOME_STRING):
        return input(string)

    @staticmethod
    def input_start(string=START_STRING):
        i = ''
        while i.upper() not in [x.upper() for x in START_EXIT_KEY_WORDS.values()]:
            i = input(string).strip()
        if i.upper() == START_EXIT_KEY_WORDS['exit']:
            raise KeyboardInterrupt

    select_string = SELECT_STRiNG+', '.join(' for '.join(map(str, (i.value, i.name))) for i in Attacks)

    @staticmethod
    def select_player_attack(string=select_string):
        while True:
            i = input(string)
            if not i:
                i = '1'
            if i.isdigit():
                i = int(i)
            if i in [a.value for a in Attacks]:
                return i
            print(WRONG_SELECT)
