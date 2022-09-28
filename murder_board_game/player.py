def guess(target, game):
    print("You guessed " + target)
    if target in [suspect.display_name.lower() for suspect in game.suspects if suspect.murderer is True]:
        print (target + " is the murderer")
        game.cycle_to_next_players_turn()
    elif target in [suspect.display_name.lower() for suspect in game.suspects]:
        print (target + " is not the murderer")
        game.cycle_to_next_players_turn()
    else:
        print(target + " is not a suspect")

def skip(game):
    # deal another hand
    print("You skipped your turn ")
    game.cycle_to_next_players_turn()
