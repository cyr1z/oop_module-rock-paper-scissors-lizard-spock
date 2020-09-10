from sys import exit
from settings import WELCOME_STRING, START_STRING, START_EXIT_KEY_WORDS, GOODBYE_STRING


class Enemy:
    """- свойства - level, lives.
    - конструктор принимает уровень. Уровень жизней противнка = уровень противника."""
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """возвращает случайное число от одного до трёх."""
        pass

    def decrease_lives(self):
        """уменьшает количество жизней. Когда жизней становится 0 вызывает
        исключение EnemyDown."""
        pass


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
    pass

    def decrease_lives(self):
        """- то  же, что и Enemy.decrease_lives(), вызывает исключение
            GameOver."""
        pass

    def attack(self, enemy_obj):
        """- получает ввод от пользователя(1, 2, 3), выбирает
            атаку противника из объекта enemy_obj;
             вызывает метод fight();
            Если результат боя 0 - вывести "It's a draw!",
            если 1 = "You attacked successfully!" и уменьшает количество жизней противника на 1,
            если - 1 = "You missed!"""
        pass

    def defence(self, enemy_obj):
        """- то же самое, что и метод attack(),
        только в метод fight первым передается атака противника,
        и при удачной атаке противника вызывается метод decrease_lives игрока."""
        pass


class Inputs:

    @staticmethod
    def input_player_name(string=WELCOME_STRING):
        return input(string)

    @staticmethod
    def input_start(string=START_STRING):
        i = ''
        while i.upper() not in [x.upper() for x in START_EXIT_KEY_WORDS.values()]:
            i = input(string).strip()
        if i == START_EXIT_KEY_WORDS['exit']:
            print(GOODBYE_STRING)
            exit()
