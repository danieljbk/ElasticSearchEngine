from flask import Flask, render_template, request, send_file
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from search import search
from data import all_pokemon

app = Flask(__name__)


@app.route("/image")
def get_image():
    filename = "images/pokemon/" + request.args.get("number") + ".png"

    return send_file(filename, mimetype="image/png")


@app.route("/")
@app.route("/index")
def index():
    """
    Search for pokemon across a variety of terms, and show 9 results for each.
    """
    search_terms = []

    num_results = 9
    pokemon_by_category = [(t, search(t, num_results)) for t in search_terms]
    return render_template(
        "index.html",
        pokemon_by_category=pokemon_by_category,
    )


@app.route("/search", methods=["GET", "POST"])
def search_single_product():
    """
    Execute a search for a specific search term.

    Return the top 50 results.
    """
    query = request.args.get("search")
    num_results = 50
    pokemon_by_category = [(query, search(query, num_results))]
    return render_template(
        "index.html",
        pokemon_by_category=pokemon_by_category,
        search_term=query,
    )


@app.route("/pokemon/<int:pokemon_id>")
def single_product(pokemon_id):
    """
    Display information about a specific pokemon
    """

    pokemon = str(all_pokemon()[pokemon_id - 1])

    return render_template(
        "pokemon.html",
        pokemon_json=pokemon,
        search_term="",
    )


app.run(host="localhost", port=8000, debug=True)
