from game_manager import GameManager

def main():
    print()
    game = GameManager()

    # game.present_suspects()
    #game.present_weapons()
    #game.get_attributes('suspects', 'weapon')
    #for suspect in game.suspects:
    #    suspect.print_attributes()
    [print(suspect) for suspect in game.suspects]

if __name__ == "__main__":
    main()
