import random

from suspect import Suspect
from presentation_mixin import PresentationMixin
from configuration_mixin import ConfigurationMixin

class GameManager(PresentationMixin, ConfigurationMixin):
    def __init__(self, seed: int = None):
        super().__init__()
        self.reset(seed)

    def reset(self, seed: int = None):
        self.game_config = self._load_config("game")
        self.suspect_draw_count = self.game_config["suspect_draw_count"]

        if self.game_config['seed'] == "random":
            seed = random.random()

        self.suspects_config = self._load_config("suspects")
        self.weapons_config = self._load_config("weapons")
        self.suspects = self._init_suspects()

        if seed is None:
            seed = self.game_config['seed']
        self.seed = seed or random.random()
        random.seed(self.seed)

        self._generate_evidence()
        self._assign_murderer()

    def _assign_murderer(self):
        murderer_index = random.randrange(self.suspect_draw_count)
        self.suspects[murderer_index].murderer = True

    def _init_from_config(self, config: dict) -> list:
        """
        Not used
        """
        item_list = []
        item_class = getattr(sys.modules[__name__], config['class_name'])
        print(item_class)
        for item_config in config['item_list']:
            item_list.append(item_class(**item_config))

    def _select_suspect_draw_count_random_items(self, item_list):
        return random.sample(item_list, self.suspect_draw_count)

    def _init_suspects(self):
        suspects = []
        self.suspect_draw_count = min(len(self.suspects_config), self.suspect_draw_count)
        # 4 possible suspects in self.suspects_config list
        # suspect_count is 3
        # random list e.g. [1, 0, 3, 2]
        # iterate through first 3 elements of random list

        # shuffle_suspect_list_from_config
        suspect_pool_count = len(self.suspects_config)
        shuffled_suspect_range = random.sample(range(suspect_pool_count), suspect_pool_count)
        
        # pick_n_suspects_to_put_into_play(4)
        for i in range(self.suspect_draw_count):
            suspect_config = self.suspects_config[shuffled_suspect_range[i]]
            suspects.append(Suspect(**suspect_config))
        return suspects

    def _generate_evidence(self):
        suspect_draw_count = self.suspect_draw_count
        random_weapons = random.sample(self.weapons_config, suspect_draw_count)
        for i in range(suspect_draw_count):
            self.suspects[i].weapon = random_weapons[i]
