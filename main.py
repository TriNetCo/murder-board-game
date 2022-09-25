from game_manager import GameManager

def main():
    print()
    game = GameManager()

    #game.present_all_game_information()
    [print(suspect) for suspect in game.suspects]

if __name__ == "__main__":
    main()
