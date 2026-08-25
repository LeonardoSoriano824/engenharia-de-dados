import pandas as pd


# ==========================
# 1. LEITURA DOS DADOS
# ==========================

df = pd.read_csv("clientes.csv")


# ==========================
# 2. ANÁLISE DOS DADOS
# ==========================

print(df.isna().sum())
print(df["idade"].mean())


# ==========================
# 3. LIMPEZA DOS DADOS
# ==========================

df["cidade"] = df["cidade"].str.title()
df["idade"] = df["idade"].fillna(df["idade"].mean())


# ==========================
# 4. TRANSFORMAÇÃO DOS DADOS
# ==========================

df["idade"] = df["idade"].astype(int)
df["adulto"] = df["idade"] >= 18


# ==========================
# 5. VISUALIZAÇÃO
# ==========================

print(df)


# ==========================
# 6. EXPORTAÇÃO DOS DADOS
# ==========================

df.to_csv("clientes_tratados.csv", index=False)