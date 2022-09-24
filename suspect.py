class Suspect:
    def __init__(self, display_name: str, location: str):
        self.display_name = display_name
        self.location = location
        self.murderer = False
        self.weapon = None

    def __repr__(self):
        class_name = self.__class__.__name__
        namespace = str(self.__dict__)
        return class_name + ": " + namespace
