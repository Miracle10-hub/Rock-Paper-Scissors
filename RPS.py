import random

def player(prev_play, opponent_history=[], play_order={}):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Build pattern memory (last 3 moves)
    if len(opponent_history) > 3:
        last_three = "".join(opponent_history[-3:])
        if last_three not in play_order:
            play_order[last_three] = []
        play_order[last_three].append(opponent_history[-1])

    # Predict next move
    if len(opponent_history) > 3:
        last_three = "".join(opponent_history[-3:])
        if last_three in play_order:
            prediction = max(set(play_order[last_three]), key=play_order[last_three].count)
        else:
            prediction = random.choice(["R", "P", "S"])
    else:
        return random.choice(["R", "P", "S"])

    # Counter prediction
    if prediction == "R":
        return "P"
    elif prediction == "P":
        return "S"
    else:
        return "R"