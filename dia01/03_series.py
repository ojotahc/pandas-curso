# %%
import pandas as pd


idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]


series_idades = pd.Series(idades)


series_idades

# %%
idades[-1]
series_idades[0]

# %%

#Os índices das series funcionam da mesma forma que as chaves de um dicionário, ou seja, podemos acessar os valores através de seus índices. O índice fica vinculado ao elemento da serie, à aquela linha.

series_idades = series_idades.sort_values()
series_idades

# %%
series_idades[0]

# %%

# Quando colocamos o iloc, estamos falando do índice no sentido de posição e não mais de chave. Assim eu navego pelas posições e não na chave associada no índice.

series_idades.iloc[-1]

# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

indexs = [
    "Téo", "maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "naty", "Nih", "Pedro", "Kozato", "Tito",
]

series_idades = pd.Series(idades, index=indexs)

series_idades

# %%
series_idades["Pedro"] #index
series_idades.iloc[0] # posição
 # iloc é navegar nas linhas, loc é navegar nos índices.
 # na series já navegamos diretamente nos índices
