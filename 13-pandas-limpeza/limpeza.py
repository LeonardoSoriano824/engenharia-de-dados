import pandas as pd


# ==========================================
# IDENTIFICAÇÃO DE VALORES AUSENTES
# ==========================================

df = pd.DataFrame({
    "nome": ["Leonardo", "Ana", "Carlos"],
    "idade": [25, None, 30]
})

print(df.isna().sum())


# ==========================================
# PREENCHIMENTO DE VALORES AUSENTES
# ==========================================

media = df["idade"].mean()

df["idade"] = df["idade"].fillna(media).astype(int)

print(df)


# ==========================================
# IDENTIFICAÇÃO DE DUPLICATAS
# ==========================================

df = pd.DataFrame({
    "nome": ["Leonardo", "Ana", "Carlos", "Ana"],
    "idade": [25, 28, 30, 28]
})

print(df.duplicated())


# ==========================================
# REMOÇÃO DE DUPLICATAS
# ==========================================

df = df.drop_duplicates()

print(df)


# ==========================================
# LIMPEZA DE TEXTOS
# ==========================================

df = pd.DataFrame({
    "nome": ["Leonardo", "Ana", "Carlos"],
    "cidade": [" Salvador ", "recife", "SALVADOR"]
})

df["cidade"] = df["cidade"].str.strip().str.title()

print(df)


# ==========================================
# CONVERSÃO DE TIPOS
# ==========================================

df = pd.DataFrame({
    "nome": ["Leonardo", "Ana", "Carlos"],
    "idade": ["25", "28", "30"]
})

df["idade"] = df["idade"].astype(int)

print(df.dtypes)