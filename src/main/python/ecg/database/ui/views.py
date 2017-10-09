from ecg.database import decks, epic_foundry_decks
from ecg.database.ui import app
from flask import jsonify

@app.route("/foundry_decks")
def foundry_decks():
    return jsonify(epic_foundry_decks)

@app.route("/tournament_decks")
def tournament_decks():
    return jsonify(decks)
