import json
import os
import textwrap

_all_pokemon = None


class PokemonData:
    def __init__(
        self,
        id_,
        number,
        name,
        type_one,
        type_two,
        max_cp,
        max_hp,
    ):
        self.id = id_
        self.number = number
        self.name = name
        self.type_one = type_one
        self.type_two = type_two
        self.max_cp = max_cp
        self.max_hp = max_hp

    def __str__(self):
        return textwrap.dedent(
            """\
            Id: {}
            number: {}
            name: {}
            type_one: {}
            type_two: {}
            max_cp: {}
            max_hp: {}
        """
        ).format(
            self.id,
            self.number,
            self.name,
            self.type_one,
            self.type_two,
            self.max_cp,
            self.max_hp,
        )


def all_pokemon():
    global _all_pokemon

    if _all_pokemon is None:
        _all_pokemon = []

        # Load the pokemon json from the same directory as this file.
        dir_path = os.path.dirname(os.path.realpath(__file__))
        pokemon_path = os.path.join(dir_path, "data/pokemons.json")
        with open(pokemon_path) as pokemon_file:
            for idx, pokemon in enumerate(json.load(pokemon_file)):
                id_ = idx + 1  # ES indexes must be positive integers, so add 1
                pokemon_data = PokemonData(id_, **pokemon)
                _all_pokemon.append(pokemon_data)

    return _all_pokemon
