import yaml

with open('configs/suspects.yml') as f:
    suspects_config = yaml.safe_load(f)

class Suspect:
    def __init__(self, display_name: str, color: str):
        self.display_name = display_name
        self.color = color
        self.murderer = False

suspects = []
for suspect_config in suspects_config:
    suspects.append(Suspect(**suspect_config))
