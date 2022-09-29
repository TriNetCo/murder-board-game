import random
import numpy as np

from murder_board_game.presentation_mixin import PresentationMixin
from murder_board_game.debug_mixin import DebugMixin

class Game(PresentationMixin, DebugMixin):
    def __init__(self, new_seed: int = None):
        super().__init__()

    def reset(self, new_seed: int = None):
        self.player_count = 3
        self.current_player = 0
        self._assign_seed(new_seed)
        self._assign_suspects()
        self._assign_evidence()
        self._assign_murderer()
        self._generate_evidence_deck()

    def _assign_seed(self, new_seed):
        if new_seed:
            self.seed = new_seed
        if self.seed == "random":
            self.seed = random.random()
        random.seed(self.seed)

    def _assign_random_evidence(self, evidence_type: str, items: list):
        random_items = random.sample(items, self.suspect_draw_count)
        for i in range(self.suspect_draw_count):
            setattr(self.suspects[i].suspect_evidence, evidence_type, random_items[i])

    def _assign_murderer(self):
        murderer_index = random.randrange(self.suspect_draw_count)
        self.suspects[murderer_index].murderer = True

    def _generate_evidence_deck(self):
        assert self._evidence_per_suspect_count > 1
        assert self.suspect_draw_count > 1
        # each innocent contributs at least one evidence card
        min_cards_per_innocent = 1
        # only the murderer contributes all evidence cards
        max_cards_per_innocent = self._evidence_per_suspect_count - 1
        innocent_count = self.suspect_draw_count - 1
        cards_to_draw_for_innocents_counts = np.round(np.linspace(min_cards_per_innocent, max_cards_per_innocent, innocent_count))
        evidence_deck = []
        counts_index = 0
        # draw from evidence
        for suspect in self.suspects:
            current_all_evidence = list(suspect.suspect_evidence.__dict__.values())
            print(current_all_evidence)
            if suspect.murderer == True:
                evidence_to_add = current_all_evidence
            else:
                current_draw_count = int(cards_to_draw_for_innocents_counts[counts_index])
                print(current_draw_count)
                counts_index = counts_index + 1
                evidence_to_add = random.sample(current_all_evidence, current_draw_count)
            evidence_deck = evidence_deck + evidence_to_add
        # shuffle
        random.shuffle(evidence_deck)
        self.evidence_deck = evidence_deck

    def _assign_suspects(self):
        self.suspects = random.sample(self.suspects_pool, self.suspect_draw_count)

    def _assign_evidence(self):
        self._assign_random_evidence("weapon", self.weapons_pool)
        self._assign_random_evidence("hair_color", self.hair_color_pool)
        self._evidence_per_suspect_count = 2
