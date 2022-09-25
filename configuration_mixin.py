import yaml
import sys
# TODO import Suspect, Evidence dynamically
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
        Loads config from YAML and instantiates list of objects based on
        class_name specified in YAML
        """
        config = self._load_config(name)
        assert 'class_name' in config and 'items' in config, "{}.yml must have class_name and items".format(name)
        class_name = config['class_name']

        current_namespace = sys.modules[__name__]
        cls = getattr(current_namespace, class_name)
        items = [cls(**item_config) for item_config in config['items']]

        return items

