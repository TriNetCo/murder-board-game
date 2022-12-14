import random
import yaml
import sys
from murder_board_game.game import Game
# TODO import Suspect, Evidence dynamically
from murder_board_game.suspect import Suspect
from murder_board_game.evidence import Evidence

def load_entities_from_config(game: Game):
    """
    Puts all the suspects, weapons, etc into the game object by parsing the yaml files.
    """
    _load_game_config(game)
    game.suspects_pool = _init_from_config("configs/suspects.yml")
    game.weapons_pool = _init_from_config("configs/weapons.yml")
    game.hair_color_pool = _init_from_config("configs/hair_color.yml")

def _load_game_config(game: Game):
    game.game_config = load_config("configs/game.yml")
    for k, v in game.game_config.items():
        setattr(game, k, v)

def load_config(filename: str) -> dict:
    """
    Loads data from a yml given the name.yml
    """
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None

def _get_class_from_config(config):
    assert 'class_name' in config, "YAML must contain field class_name"
    class_name = config['class_name']
    current_namespace = sys.modules[__name__]
    cls = getattr(current_namespace, class_name)
    return cls

def _get_item_configs_from_config(config) -> list:
    assert 'items' in config, "YAML must contain field items"
    item_configs = config['items']
    # returns empty dict if no universal_attributes in config
    universal_attributes_config = config.get('universal_attributes', {})
    # combines universal_attributes and item config, item config takes precedence
    item_configs = [{**universal_attributes_config, **item_config} for item_config in item_configs]
    return item_configs

def _init_from_config(filename: str) -> list:
    """
    Loads config from YAML and instantiates list of objects based on
    class_name specified in YAML
    """
    config = load_config(filename)
    cls = _get_class_from_config(config)
    item_configs = _get_item_configs_from_config(config)
    items = [cls(**item_config) for item_config in item_configs]
    return items
