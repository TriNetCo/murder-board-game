import random
import sys

from suspect import Suspect
from evidence import Evidence
from presentation_mixin import PresentationMixin
from configuration_utils import load_config, init_from_config
from debug_mixin import DebugMixin

class GameManager(PresentationMixin, DebugMixin):
    def __init__(self, seed: int = None):
        super().__init__()
        self.reset(seed)

    def reset(self, seed: int = None):
        self.game_config = load_config("configs/game.yml")
        self.suspect_draw_count = self.game_config["suspect_draw_count"]

        if seed is None:
            seed = self.game_config['seed']
        if seed == "random":
            seed = random.random()
        self.seed = seed or random.random()
        random.seed(self.seed)

        suspects_pool = init_from_config("configs/suspects.yml")
        self.suspects = random.sample(suspects_pool, self.suspect_draw_count)
        self._generate_evidence()
        self._assign_murderer()
                
    def _generate_evidence(self):
        weapons_pool = init_from_config("configs/weapons.yml")
        self._assign_random_evidence("weapon", weapons_pool)
        hair_color_pool = init_from_config("configs/hair_color.yml")
        self._assign_random_evidence("hair", hair_color_pool)

    def _assign_random_evidence(self, evidence_type: str, items: list):
        random_items = random.sample(items, self.suspect_draw_count)
        for i in range(self.suspect_draw_count):
            setattr(self.suspects[i], evidence_type, random_items[i])

    def _assign_murderer(self):
        murderer_index = random.randrange(self.suspect_draw_count)
        self.suspects[murderer_index].murderer = True
