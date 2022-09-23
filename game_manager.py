import yaml
import random

class GameManager():
    def __init__(self, seed: int = None):
        self.reset(seed)

    def reset(self, seed: int = None):
        self.seed = seed or random.random()
        random.seed(self.seed)
        self.suspects = self._load_config("suspects")
        self.weapons = self._load_config("weapons")
        self._generate_evidence()

    def _load_config(self, name):
        with open("configs/{}.yml".format(name), "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None

    def _load_suspects(self):
        with open("configs/suspects.yml", "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None
    
    def get_suspect_names(self):
        return '\n'.join([x['display_name'] for x in self.suspects])

    def get_attributes(self, domain_name, property_name):
        domain = getattr(self, domain_name)
        properties = [x[property_name] for x in domain]
        properties_str = ', '.join(properties)
        return properties
        #return print("{} {}s : {}".format(domain_name, property_name, properties_str))

    def present_suspects(self):
        yaml_name = 'suspects'
        items = self.get_attributes(yaml_name, 'display_name')
        print("Suspects: ")
        for item in items:
            print("  " + item)

    def present_weapons(self):
        yaml_name = 'weapons'
        items = self.get_attributes(yaml_name, 'display_name')
        print("Weapons: ")
        for item in items:
            print("  " + item)

        # print("Suspects:\n - ", "\n - ".join(self.get_attributes('suspects', 'display_name')))



    """
    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            # name = weapon_name
            return self.get_the_names(name)
        return _missing
    """
    def _generate_evidence(self):
        suspects = self.suspects
        weapons = self.weapons
        random_list = random.sample(range(len(suspects)), len(suspects))
        for i in range(len(suspects)):
            suspects[i]['weapon'] = weapons[random_list[i]]
        return
