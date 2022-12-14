from murder_board_game.debug_mixin import DebugMixin

class Evidence(DebugMixin):
    def __init__(self, display_name: str, type: str = None):
        self.display_name = display_name
        self.type = type

class SuspectEvidence(DebugMixin):
    def __init__(self):
        self.weapon = None
        self.hair_color = None
