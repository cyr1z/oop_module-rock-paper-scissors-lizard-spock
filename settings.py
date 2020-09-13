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
SELECT_STRING = 'Select your champion. Enter '
WRONG_SELECT = 'Wrong select. Enter one of this numbers: '
ENEMY_DOWN_STRING = "Enemy falling down! Your score is"
LIVES_STRING = "Your Lives is "
GAME_OVER_STRING = "Game over. Your score is "
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
