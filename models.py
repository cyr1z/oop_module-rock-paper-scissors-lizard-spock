"""
Basic models and classes for the player, types of attacks, enemies,
and a class in which user input methods
"""
from enum import Enum
from random import randint
from exceptions import EnemyDown, GameOver
from settings import WELCOME_STRING, START_STRING, COMMANDS,\
    WRONG_SELECT, SELECT_STRING, ATTACK_STRINGS, DEFENSE_STRINGS,\
    GAME_OVER_STRING, LIVES_STRING


class Attacks(Enum):
    """Enum for attacks methods"""
    robber = 1
    warrior = 2
    wizard = 3

    def __str__(self):
        return f'{self.value} for {self.name}'


class Enemy:
    """- properties - level, lives.
    - the constructor takes the level.
    Opponent's health level = opponent's level."""

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """returns a random number between one and three"""
        return randint(1, 3)

    def decrease_lives(self):
        """reduces the number of lives.
        Raises an EnemyDown exception when lives become 0."""
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
        """- same as Enemy.decrease_lives (),
        throws GameOver exception."""
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
        the player's decrease_lives method is called."""
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

    @staticmethod
    def input_start(string=START_STRING):
        """input the command 'start' or 'exit'"""
        command = ''
        while command.lower() not in COMMANDS.values():
            command = input(string).strip()
        if command.lower() == COMMANDS['exit']:
            raise KeyboardInterrupt

    # string collected Attacks names and numbers
    # for the player select one of them
    select_string = SELECT_STRING + ', '.join(str(i) for i in Attacks)

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
