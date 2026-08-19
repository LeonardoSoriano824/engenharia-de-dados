import pandas as pd

# Dados

clientes = [
    {"nome": " Leonardo ", "idade": 23, "cidade": "Salvador"},
    {"nome": "Ana", "idade": None, "cidade": "Recife"},
    {"nome": "CARLOS", "idade": 19, "cidade": "SALVADOR"},
    {"nome": "Marina", "idade": 31, "cidade": "São Paulo"}
]

df = pd.DataFrame(clientes)

# Limpeza e Transformação

df["nome"] = df["nome"].str.strip().str.title()
df["cidade"] = df["cidade"].str.strip().str.title()

df["idade"] = df["idade"].fillna(df["idade"].mean())
df["idade"] = df["idade"].astype(int)

# Resultado

print(df)
print(df.dtypes)
