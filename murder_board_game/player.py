def guess(target, game):
    print("You guessed " + target)
    if target in [suspect.display_name.lower() for suspect in game.suspects if suspect.murderer is True]:
        print (target + " is the murderer")
        _cycle_to_next_players_turn(game)
    elif target in [suspect.display_name.lower() for suspect in game.suspects]:
        print (target + " is not the murderer")
        _cycle_to_next_players_turn(game)
    else:
        print(target + " is not a suspect")

def skip(game):
    # deal another hand
    print("You skipped your turn ")
    _cycle_to_next_players_turn(game)

def list_hand(game):
    print(f"Player {game.current_player}'s hand:")
    print("TODO: implement this")

def _cycle_to_next_players_turn(game):
    game.current_player = (game.current_player + 1) % 3
