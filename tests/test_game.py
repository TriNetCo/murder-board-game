import pytest
from murder_board_game.game import Game
from murder_board_game.config import load_entities_from_config

def test_load_entities_from_config():
    game = Game()
    load_entities_from_config(game)

