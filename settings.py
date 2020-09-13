"""
SETTINGS AND STRINGS CONSTANTS
"""
LIVES = 10
ENEMY_DOWN_SCORE = 5
SCORE_FILE = 'scores.txt'
WELCOME_STRING = 'Enter your name: '
GOODBYE_STRING = 'Good bye!'
START_STRING = 'Enter "start" for play, "help" for view available commands,' \
               '"scores" for view best scores or "exit" for exit: '
AVAILABLE_COMMANDS = 'Available commands: '
SELECT_STRING = 'Select your item. Enter '
WRONG_SELECT = 'Wrong select. Enter one of this numbers: '
ENEMY_DOWN_STRING = "Enemy falling down! Your score is"
LIVES_STRING = "Your Lives is "
GAME_OVER_STRING = "Game over. Your score is "
ENEMY_CHOISE = "Enemy show "
YOUR_CHOISE = "You show "
LOSES = {
    1: (2, 5),
    2: (3, 4),
    3: (1, 5),
    4: (1, 3),
    5: (2, 4),
}
ATTACK_STRINGS = {
    -1: "You missed!",
    0: "It's a draw!",
    1: "You attacked successfully!"}
DEFENSE_STRINGS = {
    -1: "You defenced successfully!",
    0: "It's a draw!",
    1: "You missed!"}
COMMANDS = {'start': 'start',
            'exit': 'exit',
            'help': 'help',
            'scores': 'scores'}
