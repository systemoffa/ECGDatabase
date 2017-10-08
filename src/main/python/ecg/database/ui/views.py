from ecg.database import foundry_decks
from ecg.database.ui import app
from flask import jsonify

@app.route("/all_decks")
def all_decks():
    return jsonify(foundry_decks)
