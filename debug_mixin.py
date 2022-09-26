class DebugMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = str(self.__dict__)
        return class_name + ": " + attributes
