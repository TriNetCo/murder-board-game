
import yaml
import random

def main():
    game_manager = GameManager(1)
    print(game_manager.suspects)

class GameManager():
    def __init__(self, seed: int = None):
        self.reset(seed)

    def reset(self, seed: int = None):
        self.seed = seed or random.random()
        random.seed(self.seed)
        self.suspects = self.get_suspects()

    def get_suspects(self):
        print("Retrieving suspects")
        with open("configs/suspects.yml", "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None
    
    def generate_evidence(self):
        return


if __name__ == "__main__":
    main()
