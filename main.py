from game_manager import GameManager

def main():
    print()
    game = GameManager()

    game.present_all_game_information()
    # [print(suspect) for suspect in game.suspects]

    repl(game)

def repl(game):
    while(True):
        print("Ready Player 1")

        raw_input = input()
        # print("You said: " + raw_input)

        command = raw_input[0]
        # print("Command: " + command)

        if command == "h":
            print("Commands:")
            print("h - help: Displays this message")
            print("s - show hand: Shows the current players hand of cards")
            print("g - guess (<suspect's name>): The current player takes a guess at the suspect by their name.")
            print("p - pass")

        if command == 'g':
            target = raw_input[2:]
            game.guess(target)

        if command == 'p':
            game.skip()
        if command == 'q':
            print("Goodbye")
            return

        




if __name__ == "__main__":
    main()
