class Evidence:
    def __init__(self, display_name: str, type: str = None):
        self.display_name = display_name
        self.type = None

    def __repr__(self):
        class_name = self.__class__.__name__
        namespace = str(self.__dict__)
        return class_name + ": " + namespace

