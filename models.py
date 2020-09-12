"""
Basic models and classes for the player, types of attacks, enemies,
and a class in which user input methods
"""
from enum import Enum
from random import randint
from exceptions import EnemyDown, GameOver
from settings import WELCOME_STRING, START_STRING, COMMANDS,\
    WRONG_SELECT, SELECT_STRING, ATTACK_STRINGS, DEFENSE_STRINGS,\
    GAME_OVER_STRING, LIVES_STRING, AVAILABLE_COMMANDS, SCORE_FILE


class Attacks(Enum):
    """Enum for attacks methods"""
    robber = 1
    warrior = 2
    wizard = 3

    def __str__(self):
        return f'{self.value} for {self.name}'

    @classmethod
    def full_string(cls):
        """returns string with all Enum items"""
        return ', '.join(str(i) for i in cls.__iter__())


class Enemy:
    """
    - properties - level, lives.
    - the constructor takes the level.
    Opponent's health level = opponent's level.
    """
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """returns a random number between one and three"""
        return randint(1, 3)

    def decrease_lives(self):
        """
        reduces the number of lives.
        Raises an EnemyDown exception when lives become 0.
        """
        self.lives -= 1
        if not self.lives:
            raise EnemyDown


class Player:
    """
    Class for creating a player object that stores name, points, lives
    and has attack and defense battle methods
    :param name: Player name
    :param lives: How many lives at start Player has
    """
    def __init__(self, name, lives):
        self.score = 0
        self.name = name
        self.lives = lives

    @staticmethod
    def fight(attack, defense):
        """
        :param attack: int number attack type
        :param defense: int number defense type
        :return: returns the result of the round
                0 if there is a draw,
                -1 if the attack is unsuccessful,
                1 if the attack is successful.
        """
        # draw
        if attack == defense:
            return 0
        # lose
        if attack == 1 and defense == 2:
            return -1
        if attack == 2 and defense == 3:
            return -1
        if attack == 3 and defense == 1:
            return -1
        # won
        return 1

    def decrease_lives(self):
        """
        - same as Enemy.decrease_lives (),
        throws GameOver exception.
        """
        self.lives -= 1
        if not self.lives:
            print(GAME_OVER_STRING, self.score)
            print(LIVES_STRING, self.lives)
            raise GameOver

    def attack(self, enemy_obj: Enemy):
        """
        - receives input from user (1, 2, 3),
         selects enemy attack from enemy_obj object;
        calls the fight () method;
        If the result of the battle is 0, print "It's a draw!",
        If 1 = "You attacked successfully!"
        and reduces the number of enemy lives by 1, if - 1 = "You missed!
        :param enemy_obj: Enemy object for fight with player
        """
        my_choice = Inputs.select_player_attack()
        result = self.fight(my_choice, enemy_obj.select_attack())
        print(ATTACK_STRINGS[result])
        if result == 1:
            enemy_obj.decrease_lives()
            self.score += 1

    def defence(self, enemy_obj: Enemy):
        """
        :param enemy_obj: Enemy object for fight with player
        - the same as the attack () method,
        only the opponent's attack is passed to the fight method first,
        and if the opponent's attack is successful,
        the player's decrease_lives method is called.
        """
        my_choice = Inputs.select_player_attack()
        result = self.fight(enemy_obj.select_attack(), my_choice)
        print(DEFENSE_STRINGS[result])
        if result == 1:
            self.decrease_lives()


class Inputs:
    """class in which user input methods"""
    @staticmethod
    def input_player_name(string=WELCOME_STRING):
        """player name input"""
        return input(string)

    @classmethod
    def input_start(cls, string=START_STRING):
        """input the command 'start', 'help', 'scores' or 'exit'"""
        command = ''
        while command not in COMMANDS.values():
            command = input(string).strip().lower()
        if command == COMMANDS['exit']:
            raise KeyboardInterrupt
        if command == COMMANDS['help']:
            print(AVAILABLE_COMMANDS)
            print(*COMMANDS.values(), sep=', ')
            cls.input_start()
        if command == COMMANDS['scores']:
            scores = Scores()
            scores.read_from_file(SCORE_FILE)
            print(scores)
            cls.input_start()

    # string collected Attacks names and numbers
    # for the player select one of them
    select_string = f'{SELECT_STRING} {Attacks.full_string()}: '

    @staticmethod
    def select_player_attack(string=select_string):
        """player selects the type of attack"""
        while True:
            i = input(string)
            if not i:
                i = '1'
            if i.isdigit():
                i = int(i)
            if i in [a.value for a in Attacks]:
                return i
            print(WRONG_SELECT)


class Scores(dict):
    """scores dict with file read/write methods and __str__ """
    def read_from_file(self, score_file):
        """
        Read scores from file.
        :param score_file: file name
        :return: nothing. Only get items to internal dictionary.
        """
        with open(score_file, "r") as s_file:
            scores_string = s_file.readlines()
            for i in scores_string:
                i = i.strip().split(': ')
                self[i[0]] = int(i[1])

    def sorted(self):
        """return sorted scores"""
        return sorted(self.items(), key=lambda x: x[1], reverse=True)

    def new_result(self, player: Player, score_file):
        """
        working with new score result
        :param player: Player object having 'name' and 'score' parameters
        :param score_file: file name
        :return: nothing/ renew score file and internal dictionary
        """
        if player.name not in self:
            self[player.name] = player.score
            with open(score_file, "a") as s_file:
                s_file.write(f'{player.name}: {player.score}\n')
        elif self[player.name] < player.score:
            self[player.name] = player.score
            with open(score_file, "w") as s_file:
                for key, value in self.sorted():
                    s_file.write(f'{key}: {value}\n')

    def __str__(self):
        return '\n'.join(f'{key}: {value}' for key, value in self.sorted())
