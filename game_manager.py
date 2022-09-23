import yaml
import random

class GameManager():
    def __init__(self, seed: int = None):
        self.reset(seed)

    def reset(self, seed: int = None):
        self.seed = seed or random.random()
        random.seed(self.seed)
        self.suspects = self._get_suspects()
        self._generate_evidence()

    def _get_suspects(self):
        print("Retrieving suspects")
        with open("configs/suspects.yml", "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None
    
    def _generate_evidence(self):
        return
