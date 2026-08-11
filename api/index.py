from flask import Flask, request, jsonify, send_from_directory
import random

app = Flask(__name__, static_folder="../static", static_url_path="/static")

CARDS = [
    "R1","R2","R3","R4","R5","R6","R7","R8","R9","Rskip","Rreverse","u+4","R+1","U",
    "B1","B2","B3","B4","B5","B6","B7","B8","B9","Bskip","Breverse","u+4","B+1","U",
    "G1","G2","G3","G4","G5","G6","G7","G8","G9","Gskip","Greverse","u+4","G+1","U",
    "Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9","Yskip","Yreverse","u+4","Y+1","U",
]
STARTING_CARDS = [f"{c}{n}" for c in "RBGY" for n in range(1,10)]

def draw(hand, amount=1):
    for _ in range(amount):
        hand.append(random.choice(CARDS))

def make_game(opponents):
    hands = [random.sample(CARDS, 7) for _ in range(opponents + 1)]
    return {
        "hands": hands,
        "last_card": random.choice(STARTING_CARDS),
        "penalty": 0,
        "current": 0,
        "direction": 1,
        "opponents": opponents,
        "winner": None,
        "log": ["Game started.", f"Starting card: {hands and random.choice(STARTING_CARDS)}"],
        "last_event": None,
    }

def event(g, text, kind="info"):
    g["log"].append(text)
    g["log"] = g["log"][-14:]
    g["last_event"] = {"text": text, "kind": kind}

def next_player(g, steps=1):
    return (g["current"] + g["direction"] * steps) % len(g["hands"])

def is_plus(card):
    return card[1:] == "+1" or card == "u+4"

def system_turn(g):
    """Direct translation of the supplied system-turn rules."""
    if g["winner"] is not None:
        return

    system_no = g["current"]
    hand = g["hands"][system_no]

    if not hand:
        g["winner"] = system_no
        event(g, f"System {system_no} won!", "win")
        return

    # Penalty logic: stack if possible, otherwise take penalty.
    if g["penalty"] > 0:
        stack_cards = [c for c in hand if is_plus(c)]
        if stack_cards:
            card = random.choice(stack_cards)
            if card[1:] == "+1":
                hand.remove(card)
                g["last_card"] = card
                g["penalty"] += 1
                event(g, f"System {system_no} stacked +1", "penalty")
            else:
                hand.remove(card)
                color = random.choice(["R", "B", "G", "Y"])
                g["last_card"] = color + "0"
                g["penalty"] += 4
                event(g, f"System {system_no} stacked +4 and chose {color}", "penalty")
            if not hand:
                g["winner"] = system_no
                event(g, f"System {system_no} won!", "win")
                return
            g["current"] = next_player(g)
            return
        else:
            amount = g["penalty"]
            draw(hand, amount)
            event(g, f"System {system_no} took {amount} penalty cards.", "draw")
            g["penalty"] = 0
            g["current"] = next_player(g)
            return

    possible = [
        c for c in hand
        if c[0] == g["last_card"][0]
        or c[1:] == g["last_card"][1:]
        or c == "U"
        or c == "u+4"
    ]

    if not possible:
        extra = random.choice(CARDS)
        hand.append(extra)
        event(g, f"System {system_no} had no valid card and drew {extra}.", "draw")
        g["current"] = next_player(g)
        return

    card = random.choice(possible)
    hand.remove(card)
    event(g, f"System {system_no} played {card}.", "play")

    if card == "U":
        color = random.choice(["R", "B", "G", "Y"])
        g["last_card"] = color + "0"
        event(g, f"System {system_no} chose {color}.", "wild")
        g["current"] = next_player(g)
        return

    if card == "u+4":
        color = random.choice(["R", "B", "G", "Y"])
        g["last_card"] = color + "0"
        g["penalty"] += 4
        event(g, f"System {system_no} played +4 and chose {color}.", "penalty")
        g["current"] = next_player(g)
        return

    g["last_card"] = card

    if card[1:] == "+1":
        g["penalty"] += 1
        event(g, f"System {system_no} played +1. Penalty: {g['penalty']}", "penalty")
        g["current"] = next_player(g)
    elif card[1:] == "reverse":
        g["direction"] *= -1
        event(g, "Direction reversed.", "reverse")
        g["current"] = next_player(g)
    elif card[1:] == "skip":
        event(g, "Next player skipped.", "skip")
        g["current"] = next_player(g, 2)
    else:
        g["current"] = next_player(g)

    if not hand:
        g["winner"] = system_no
        event(g, f"System {system_no} won!", "win")

def player_turn(g, action, color=None):
    hand = g["hands"][0]

    if g["winner"] is not None:
        return {"ok": False, "message": "Game already ended."}

    if not action:
        return {"ok": False, "message": "Choose a card or Draw."}

    # Penalty logic exactly follows the supplied 4-system version.
    if g["penalty"] > 0:
        stack_cards = [c for c in hand if is_plus(c)]
        if stack_cards:
            if action in stack_cards:
                if action[1:] == "+1":
                    hand.remove(action)
                    g["last_card"] = action
                    g["penalty"] += 1
                    event(g, "You stacked +1.", "penalty")
                elif action == "u+4":
                    if color not in ["R","B","G","Y"]:
                        return {"ok": False, "message": "Choose a valid color."}
                    hand.remove(action)
                    g["last_card"] = color + "0"
                    g["penalty"] += 4
                    event(g, f"You stacked +4 and chose {color}.", "penalty")
                else:
                    return {"ok": False, "message": "Invalid penalty card."}
                if not hand:
                    g["winner"] = 0
                    event(g, "YOU WON!", "win")
                    return {"ok": True}
                g["current"] = next_player(g)
                return {"ok": True}
            if action.lower() == "x":
                amount = g["penalty"]
                draw(hand, amount)
                g["penalty"] = 0
                event(g, f"You took {amount} penalty cards.", "draw")
                g["current"] = next_player(g)
                return {"ok": True}
            return {"ok": False, "message": "You must stack or take the penalty."}
        else:
            amount = g["penalty"]
            draw(hand, amount)
            g["penalty"] = 0
            event(g, f"You took {amount} penalty cards.", "draw")
            g["current"] = next_player(g)
            return {"ok": True}

    if action.lower() == "x":
        extra = random.choice(CARDS)
        hand.append(extra)
        event(g, f"You drew {extra}.", "draw")
        g["current"] = next_player(g)
        return {"ok": True, "drawn": extra}

    if action not in hand:
        return {"ok": False, "message": "You don't have that card."}

    if action == "U":
        if color not in ["R","B","G","Y"]:
            return {"ok": False, "message": "Choose a valid color."}
        hand.remove(action)
        g["last_card"] = color + "0"
        event(g, f"You played WILD and chose {color}.", "wild")
        if not hand:
            g["winner"] = 0
            event(g, "YOU WON!", "win")
            return {"ok": True}
        g["current"] = next_player(g)
        return {"ok": True}

    if action == "u+4":
        if color not in ["R","B","G","Y"]:
            return {"ok": False, "message": "Choose a valid color."}
        hand.remove(action)
        g["last_card"] = color + "0"
        g["penalty"] += 4
        event(g, f"You played +4 and chose {color}.", "penalty")
        if not hand:
            g["winner"] = 0
            event(g, "YOU WON!", "win")
            return {"ok": True}
        g["current"] = next_player(g)
        return {"ok": True}

    if action[0] == g["last_card"][0] or action[1:] == g["last_card"][1:]:
        hand.remove(action)
        g["last_card"] = action
        event(g, f"You played {action}.", "play")

        if action[1:] == "+1":
            g["penalty"] += 1
            event(g, f"Penalty: {g['penalty']}", "penalty")
            g["current"] = next_player(g)
        elif action[1:] == "reverse":
            g["direction"] *= -1
            event(g, "Direction reversed.", "reverse")
            g["current"] = next_player(g)
        elif action[1:] == "skip":
            event(g, "Next player skipped.", "skip")
            g["current"] = next_player(g, 2)
        else:
            g["current"] = next_player(g)

        if not hand:
            g["winner"] = 0
            event(g, "YOU WON!", "win")
        return {"ok": True}

    # Supplied rule: invalid card causes one extra card.
    extra = random.choice(CARDS)
    hand.append(extra)
    event(g, f"Invalid card. You took {extra}.", "invalid")
    g["current"] = next_player(g)
    return {"ok": True, "drawn": extra}

@app.get("/")
def home():
    return send_from_directory("../static", "index.html")

@app.get("/api/health")
def health():
    return jsonify({"ok": True})

@app.post("/api/new")
def new_game():
    data = request.get_json(silent=True) or {}
    opponents = int(data.get("opponents", 1))
    opponents = max(1, min(4, opponents))
    return jsonify({"game": make_game(opponents)})

@app.post("/api/action")
def action():
    data = request.get_json(silent=True) or {}
    game = data.get("game")
    if not game:
        return jsonify({"ok": False, "message": "Game state missing."}), 400

    if game["winner"] is not None:
        return jsonify({"ok": False, "message": "Game already ended.", "game": game})

    if game["current"] != 0:
        return jsonify({"ok": False, "message": "Wait for the system turn.", "game": game})

    result = player_turn(game, data.get("action"), data.get("color"))

    # Run AI turns immediately, with a short delay handled visually by the client.
    while game["winner"] is None and game["current"] != 0:
        system_turn(game)

    return jsonify({**result, "game": game})

if __name__ == "__main__":
    app.run(debug=True)
