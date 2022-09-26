from debug_mixin import DebugMixin

class Suspect(DebugMixin):
    def __init__(self, display_name: str, location: str):
        self.display_name = display_name
        self.location = location
        self.murderer = False
        self.weapon = None
