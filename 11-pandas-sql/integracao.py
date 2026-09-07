import sqlite3

import pandas as pd


# ==========================================
# CONEXÃO COM O BANCO
# ==========================================

conexao = sqlite3.connect("clientes.db")

cursor = conexao.cursor()


# ==========================================
# CRIAÇÃO DA TABELA
# ==========================================

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        cidade TEXT
    )
''')

conexao.commit()


# ==========================================
# EXTRAÇÃO DOS DADOS COM SQL
# ==========================================

dados = cursor.execute("""
    SELECT *
    FROM clientes
""").fetchall()


# ==========================================
# CONVERSÃO PARA PANDAS
# ==========================================

df = pd.DataFrame(
    dados,
    columns=("id", "nome", "idade", "cidade")
)


# ==========================================
# FILTROS COM PANDAS
# ==========================================

clientes_maiores = df[df["idade"] >= 25]

clientes_salvador = df[
    (df["cidade"] == "Salvador") &
    (df["idade"] > 23)
]


# ==========================================
# AGRUPAMENTOS COM PANDAS
# ==========================================

clientes_por_cidade = df.groupby("cidade")["id"].count()

idade_media_cidade = df.groupby("cidade")["idade"].mean()

analise_cidades = df.groupby("cidade")[["id", "idade"]].agg({
    "id": "count",
    "idade": "mean"
})


# ==========================================
# SQL DIRETAMENTE PARA PANDAS
# ==========================================

clientes_25 = pd.read_sql_query("""
    SELECT nome, idade
    FROM clientes
    WHERE idade >= 25
""", conexao)


clientes_salvador_sql = pd.read_sql_query("""
    SELECT *
    FROM clientes
    WHERE cidade = "Salvador"
""" , conexao)


# ==========================================
# ANÁLISE COM PANDAS APÓS SQL
# ==========================================

analise_idade = clientes_salvador_sql["idade"].mean()


# ==========================================
# ANÁLISE DE RECIFE
# ==========================================

recife_idade_maxima = pd.read_sql_query("""
    SELECT cidade, nome, idade
    FROM clientes
    WHERE cidade = 'Recife'
""", conexao)

recife_idade_maxima = recife_idade_maxima["idade"].max()

print(f"Maior idade em Recife: {recife_idade_maxima}")


# ==========================================
# FECHAMENTO
# ==========================================

conexao.close()