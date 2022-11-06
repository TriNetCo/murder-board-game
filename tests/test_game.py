# run pytest tests/game_test.py
import pytest
from murder_board_game.game import Game
from murder_board_game.config import load_entities_from_config

def load_entities_from_config_test():
    game = Game()
    load_entities_from_config(game)
    suspect_display_names = [suspect.display_name for suspect in game.suspects_pool]
    for suspect in ['Gangster', 'Outlaw', 'Kona', 'Bartender']:
        fail_message = "{} not in suspect display names: {}".format(suspect, str(suspect_display_names))
        assert suspect in suspect_display_names, fail_message
