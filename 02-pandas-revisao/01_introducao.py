import pandas as pd

clientes = [
    {"nome": "Leonardo", "idade": 23, "cidade": "Salvador"},
    {"nome": "Ana", "idade": 28, "cidade": "Recife"},
    {"nome": "Carlos", "idade": 19, "cidade": "Salvador"},
    {"nome": "Marina", "idade": 31, "cidade": "São Paulo"}
]

df = pd.DataFrame(clientes)

# print(df)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

# print(df["nome"])
# print(df["idade"])

# Solução usando Python puro
# for cliente in clientes: 
#     if cliente["idade"] >= 25:
#         print(cliente["nome"], cliente["idade"])

# Solução usando Pandas
# print(df[df["idade"] >= 25])

# print(df[df["cidade"] == "Salvador"])

# print(df[(df["cidade"] == "Salvador") & (df["idade"] > 20)])


df["adulto"] = df["idade"] >= 18

print(df)
