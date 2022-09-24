import yaml
import random

from suspect import Suspect

class GameManager():
    def __init__(self, seed: int = None):
        self.reset(seed)

    def reset(self, seed: int = None):
        self.game_config = self._load_config("game")

        if self.game_config['seed'] == "random":
            seed = random.random()

        if seed is None:
            seed = self.game_config['seed']
        self.seed = seed or random.random()
        random.seed(self.seed)

        self.suspects_config = self._load_config("suspects")
        self.suspects = self._init_suspects()
        self.weapons_config = self._load_config("weapons")
        self._generate_evidence()



    def _load_config(self, name):
        with open("configs/{}.yml".format(name), "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None

    def _init_suspects(self):
        suspects = []
        self.game_config["suspect_draw_count"] = min(len(self.suspects_config), self.game_config["suspect_draw_count"])
        # 4 possible suspects in self.suspects_config list
        # suspect_count is 3
        # random list e.g. [1, 0, 3, 2]
        # iterate through first 3 elements of random list

        # shuffle_suspect_list_from_config
        suspect_pool_count = len(self.suspects_config)
        shuffled_suspect_range = random.sample(range(suspect_pool_count), suspect_pool_count)
        
        # pick_n_suspects_to_put_into_play(4)
        for i in range(self.game_config["suspect_draw_count"]):
            suspect_config = self.suspects_config[shuffled_suspect_range[i]]
            suspects.append(Suspect(**suspect_config))
        return suspects

    def _generate_evidence(self):
        suspect_draw_count = self.game_config["suspect_draw_count"]
        random_weapons = random.sample(self.weapons_config, suspect_draw_count)
        for i in range(suspect_draw_count):
            self.suspects[i].weapon = random_weapons[i]

    def get_attributes(self, domain_name, property_name):
        domain = getattr(self, domain_name)
        if hasattr(domain[0], property_name):
            properties = [str(getattr(x, property_name)) for x in domain]
        else:
            properties = [str(x[property_name]) for x in domain]
        properties_str = ", ".join(properties)
        print(f"{domain_name} {property_name}: {properties_str}")

    def present_suspects(self):
        print("Suspects: ")
        for suspect in self.suspects:
            print("  " + suspect.display_name)
        print()
        
    def present_weapons(self):
        yaml_name = 'weapons'
        items = self.get_attributes(yaml_name, 'display_name')
        print("Weapons: ")
        for item in items:
            print("  " + item)
        print()
        
    """
    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            # name = weapon_name
            return self.get_the_names(name)
        return _missing
    """
