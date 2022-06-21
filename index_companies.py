from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from constants import DOC_TYPE, INDEX_NAME
from data import all_pokemon, PokemonData


def pokemon_to_index():
    for pokemon in all_pokemon():
        yield {
            "_op_type": "index",
            "_index": INDEX_NAME,
            "_id": pokemon.id,
            "_source": {
                "number": pokemon.number,
                "name": pokemon.name,
                "type_one": pokemon.type_one,
                "type_two": pokemon.type_two,
                "max_cp": pokemon.max_cp,
                "max_hp": pokemon.max_hp,
            },
        }


def main():
    # Connects to localhost:9200 by default.
    es = Elasticsearch(
        hosts=["http://localhost:9200"],
        http_auth=("elastic", "BOUGSd4No0SuDBjLe77I"),  # username, password
    )

    es.indices.delete(index=INDEX_NAME, ignore=404)
    es.indices.create(
        index=INDEX_NAME,
        body={
            "mappings": {
                "properties": {
                    "number": {"type": "integer"},
                    "name": {"type": "text"},
                    "type_one": {"type": "text"},
                    "type_two": {"type": "text"},
                    "max_cp": {"type": "integer"},
                    "max_hp": {"type": "integer"},
                },
            },
        },
    )
    bulk(es, pokemon_to_index())


if __name__ == "__main__":
    main()
