from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open("mandarin_flashcards_by_chapter.json", encoding="utf-8") as f:
    flashcards = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cards")
def cards():
    return jsonify(flashcards)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
