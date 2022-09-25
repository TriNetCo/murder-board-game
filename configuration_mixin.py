import yaml

class ConfigurationMixin():
    def __init__(self):
        print("Hello from Config mixin")

    def _load_config(self, name: str) -> dict:
        with open("configs/{}.yml".format(name), "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None
