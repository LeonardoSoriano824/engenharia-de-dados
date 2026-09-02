import logging
import sqlite3

import pandas as pd


# ==========================================
# CONFIGURAÇÃO DO LOG
# ==========================================

logger = logging.getLogger(__name__)


# ==========================================
# CONEXÃO COM O BANCO
# ==========================================

def conectar_banco():
    conexao = sqlite3.connect("clientes.db")

    logger.info("Banco conectado!")

    return conexao


# ==========================================
# CRIAÇÃO DA TABELA
# ==========================================

def criar_tabela(conexao):
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        cidade TEXT
    )
    """)

    conexao.commit()

    logger.info("Tabela criada!")


# ==========================================
# LIMPEZA DO BANCO
# ==========================================

def limpar_banco(conexao):
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM clientes")

    conexao.commit()

    logger.info("Dados antigos removidos!")


# ==========================================
# EXTRAÇÃO DOS DADOS
# ==========================================

def extrair_dados():
    dados = pd.read_csv("clientes.csv")

    logger.info(f"Dados extraídos: {len(dados)} registros!")

    print(dados)

    return dados


# ==========================================
# TRANSFORMAÇÃO DOS DADOS
# ==========================================

def transformar_dados(dados):
    dados["nome"] = dados["nome"].str.strip()

    dados["cidade"] = dados["cidade"].str.strip()

    media_idade = dados["idade"].mean()

    dados["idade"] = dados["idade"].fillna(media_idade)

    dados["idade"] = dados["idade"].astype(int)

    logger.info("Dados transformados!")

    print(dados)

    return dados


# ==========================================
# VALIDAÇÃO DOS DADOS
# ==========================================

def validar_dados(dados):

    if dados.isnull().sum().sum() > 0:
        raise ValueError("Existem dados vazios!")

    if (dados["idade"] < 0).any():
        raise ValueError("Existem idades inválidas!")

    logger.info("Dados validados com sucesso!")


# ==========================================
# CARGA DOS DADOS NO BANCO
# ==========================================

def carregar_no_banco(conexao, dados):
    dados.to_sql(
        "clientes",
        conexao,
        if_exists="append",
        index=False
    )

    logger.info(f"Dados carregados: {len(dados)} registros!")


# ==========================================
# FECHAMENTO
# ==========================================

def fechar_banco(conexao):
    conexao.close()

    logger.info("Banco fechado!")