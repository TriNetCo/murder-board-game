from murder_board_game.debug_mixin import DebugMixin
from murder_board_game.evidence import SuspectEvidence

class Suspect(DebugMixin):
    def __init__(self, display_name: str, location: str):
        self.display_name = display_name
        self.location = location
        self.murderer = False
        # self.weapon = None
        # self.hair_color = None
        self.suspect_evidence = SuspectEvidence()
