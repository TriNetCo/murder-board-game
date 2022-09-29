from murder_board_game.game import Game
from murder_board_game.player import guess, skip, list_hand

from murder_board_game.config import load_entities_from_config

def main():
    print()
    game = Game()
    load_entities_from_config(game)

    game.reset()

    game.present_all_game_information()
    # [print(suspect) for suspect in game.suspects]
    repl(game)

def repl(game):
    while(True):
        print(f"Ready Player {game.current_player+1}")

        raw_input = input()
        command = raw_input[0]

        if command == "h":
            print("Commands:")
            print("h - help: Displays this message")
            print("l - List: List the current player's hand")
            print("s - show hand: Shows the current players hand of cards")
            print("g - guess (<suspect's name>): The current player takes a guess at the suspect by their name.")
            print("p - pass")

        if command == 'l':
            list_hand(game)
        if command == 'g':
            target = raw_input[2:].lower()
            guess(target, game)
        if command == 's':
            game.present_all_game_information()
        if command == 'p':
            skip(game)
        if command == 'q':
            print("Goodbye")
            return

if __name__ == "__main__":
    main()
