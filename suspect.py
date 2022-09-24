class Suspect:
    def __init__(self, display_name: str, location: str):
        self.display_name = display_name
        self.location = location
        self.murderer = False
        self.weapon = None

#suspects = []
#for suspect_config in suspects_config:
#    suspects.append(Suspect(**suspect_config))
