import yaml
import sys
from suspect import Suspect
from evidence import Evidence

class ConfigurationMixin():
    def __init__(self):
        print("Hello from Config mixin")

    def _load_config(self, name: str) -> dict:
        """
        Loads data from a yml given the name.yml
        """
        with open("configs/{}.yml".format(name), "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None

    def _init_from_config(self, name: str) -> list:
        """
        """
        config = self._load_config(name)
        assert 'class_name' in config and 'item_list' in config, "{}.yml must have class_name and item_list".format(name)
        class_name = config['class_name']
        assert hasattr(sys.modules[__name__], class_name), "{} not found in namespace".format(class_name)
        item_class = getattr(sys.modules[__name__], class_name)
        item_list = [item_class(**item_config) for item_config in config['item_list']]
        return item_list
