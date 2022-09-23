from game_manager import GameManager

def main():
    print()

    game = GameManager(1)
    # print(game.get_suspect_names())

    game.present_suspects()
    print()
    game.present_weapons()

    # print(game.get_suspect_names())
    # print(game.get_weapon_names())
    # print(game.get_weapon_names())
    # print(game.weapons)


if __name__ == "__main__":
    main()
