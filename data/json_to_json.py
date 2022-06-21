import pandas as pd

df = pd.read_json(
    "/Users/daniel/Library/Mobile Documents/com~apple~CloudDocs/Daniel's Files/Coding/Projects/Python/Search Engine/pycon-2018-pyelasticsearch/pokemons/data/pokemons.json",
    orient="columns",
)

df.to_json(
    "/Users/daniel/Library/Mobile Documents/com~apple~CloudDocs/Daniel's Files/Coding/Projects/Python/Search Engine/pycon-2018-pyelasticsearch/pokemons/data/pokemons.json",
    orient="records",
)
