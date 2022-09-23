
import yaml

def main():
    suspects = get_suspects()

    print(suspects)



def get_suspects():
    with open("configs/suspects.yml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None



main()
