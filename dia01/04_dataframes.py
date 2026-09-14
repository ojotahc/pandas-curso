# %%

import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    "Téo", "maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "naty", "Nih", "Pedro", "Kozato", "Tito",
]

# %%
series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame() # conjunto de series
df["idades"] = series_idades
df["nomes"] = series_nomes

df

# %%

df["idades"]

# %%
df.iloc[0]["nomes"] 

# %%
df.iloc[-1]["nomes"]

# Quando acesso coluna ou linha do meu dataframe, irá resultar em uma serie