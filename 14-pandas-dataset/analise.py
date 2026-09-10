import pandas as pd


# ==========================================
# CRIAÇÃO DO DATAFRAME
# ==========================================

df = pd.DataFrame({
    "produto": [
        "Notebook",
        "Mouse",
        "Teclado",
        "Notebook",
        "Mouse"
    ],
    "categoria": [
        "Eletrônicos",
        "Periféricos",
        "Periféricos",
        "Eletrônicos",
        "Periféricos"
    ],
    "preco": [3500, 80, 150, 3500, 80],
    "quantidade": [2, 10, 5, 1, 8]
})


# ==========================================
# INSPEÇÃO DOS DADOS
# ==========================================

print(df)

print(df.shape)

print(df.dtypes)


# ==========================================
# CÁLCULO DO FATURAMENTO
# ==========================================

df["faturamento"] = df["preco"] * df["quantidade"]

print(df)


# ==========================================
# MAIOR FATURAMENTO INDIVIDUAL
# ==========================================

maior_faturamento = df["faturamento"].max()

print(f"Maior faturamento individual: R$ {maior_faturamento}")


# ==========================================
# FATURAMENTO POR PRODUTO
# ==========================================

faturamento_produto = (
    df.groupby("produto")["faturamento"].sum()
)

print(faturamento_produto)


# ==========================================
# FATURAMENTO POR CATEGORIA
# ==========================================

faturamento_categoria = (
    df.groupby("categoria")["faturamento"].sum()
)

print(faturamento_categoria)


# ==========================================
# QUANTIDADE VENDIDA POR PRODUTO
# ==========================================

quantidade_produto = (
    df.groupby("produto")["quantidade"].sum()
)

print(quantidade_produto)


# ==========================================
# FATURAMENTO TOTAL
# ==========================================

faturamento_total = df["faturamento"].sum()

print(f"Faturamento total: R$ {faturamento_total}")