import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie"
        elif (
            (p1_play == "R" and p2_play == "S") or
            (p1_play == "P" and p2_play == "R") or
            (p1_play == "S" and p2_play == "P")
        ):
            results["p1"] += 1
            winner = "Player 1"
        else:
            results["p2"] += 1
            winner = "Player 2"

        if verbose:
            print(f"Player 1: {p1_play} | Player 2: {p2_play} -> {winner}")

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    print("\nFinal Results:")
    print(results)

    win_rate = results["p1"] / num_games * 100
    print(f"Win rate: {win_rate:.2f}%")

    return win_rate


# ------------------ BOTS ------------------

def quincy(prev_play):
    plays = ["R", "R", "P", "P", "S"]
    if not hasattr(quincy, "counter"):
        quincy.counter = 0
    move = plays[quincy.counter % len(plays)]
    quincy.counter += 1
    return move


def abbey(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 2:
        return "R"

    last_two = "".join(opponent_history[-2:])
    potential = {"RR": "P", "RP": "P", "RS": "R",
                 "PR": "S", "PP": "S", "PS": "P",
                 "SR": "R", "SP": "R", "SS": "S"}

    return potential.get(last_two, "R")


def kris(prev_play):
    if not hasattr(kris, "last"):
        kris.last = "R"

    counter = {"R": "P", "P": "S", "S": "R"}
    kris.last = counter[kris.last]
    return kris.last


def mrugesh(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 10:
        return random.choice(["R", "P", "S"])

    most_common = max(set(opponent_history), key=opponent_history.count)

    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[most_common]