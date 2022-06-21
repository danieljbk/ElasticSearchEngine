import pandas as pd

df = pd.read_csv(
    "/Users/daniel/Library/Mobile Documents/com~apple~CloudDocs/Daniel's Files/Coding/Projects/Python/Search Engine/pycon-2018-pyelasticsearch/pokemons/pokemons.csv"
)
df.to_json(
    "/Users/daniel/Library/Mobile Documents/com~apple~CloudDocs/Daniel's Files/Coding/Projects/Python/Search Engine/pycon-2018-pyelasticsearch/pokemons/pokemons.json",
    orient="records",
)
