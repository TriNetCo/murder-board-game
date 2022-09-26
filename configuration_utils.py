import yaml
import sys
# TODO import Suspect, Evidence dynamically
from suspect import Suspect
from evidence import Evidence

def load_config(filename: str) -> dict:
    """
    Loads data from a yml given the name.yml
    """
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None

def init_from_config(filename: str) -> list:
    """
    Loads config from YAML and instantiates list of objects based on
    class_name specified in YAML
    """
    config = load_config(filename)
    assert 'class_name' in config and 'items' in config, "{}.yml must have class_name and items".format(filename)
    class_name = config['class_name']

    current_namespace = sys.modules[__name__]
    cls = getattr(current_namespace, class_name)
    items = [cls(**item_config) for item_config in config['items']]

    return items
