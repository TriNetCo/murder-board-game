import random

from presentation_mixin import PresentationMixin
from configuration_utils import load_config, init_from_config
from debug_mixin import DebugMixin

class GameManager(PresentationMixin, DebugMixin):
    def __init__(self, new_seed: int = None):
        super().__init__()
        self.reset(new_seed)

    def reset(self, new_seed: int = None):
        self._load_game_config()
        self._assign_seed(new_seed)
        self._generate_suspects()
        self._generate_evidence()
        self._assign_murderer()

    def _load_game_config(self):
        self.game_config = load_config("configs/game.yml")
        for k, v in self.game_config.items():
            setattr(self, k, v)

    def _assign_seed(self, new_seed):
        if new_seed:
            self.seed = new_seed
        if self.seed == "random":
            self.seed = random.random()
        random.seed(self.seed)

    def _generate_suspects(self):
        suspects_pool = init_from_config("configs/suspects.yml")
        self.suspects = random.sample(suspects_pool, self.suspect_draw_count)

    def _generate_evidence(self):
        weapons_pool = init_from_config("configs/weapons.yml")
        self._assign_random_evidence("weapon", weapons_pool)
        hair_color_pool = init_from_config("configs/hair_color.yml")
        self._assign_random_evidence("hair_color", hair_color_pool)

    def _assign_random_evidence(self, evidence_type: str, items: list):
        random_items = random.sample(items, self.suspect_draw_count)
        for i in range(self.suspect_draw_count):
            setattr(self.suspects[i], evidence_type, random_items[i])

    def _assign_murderer(self):
        murderer_index = random.randrange(self.suspect_draw_count)
        self.suspects[murderer_index].murderer = True
