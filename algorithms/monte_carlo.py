# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from queue import PriorityQueue

# Personal Libraries
from core.game import Game
from core.logic import Logic

class MonteCarlo(threading.Thread):
    def __init__(self, game, callback=lambda: None):
        threading.Thread.__init__(self)
        self.game = game
        self.callback = callback