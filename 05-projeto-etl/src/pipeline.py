import sqlite3

import pandas as pd

import numpy as np

import logging


# ==========================
# CONFIGURAÇÃO DO LOG
# ==========================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s - %(asctime)s"
)


# ==========================
# 1. CARREGAMENTO DOS DADOS
# ==========================

def carregar_dados():

    try:

        dados = pd.read_csv("dados/vendas_sujas.csv")

        quantidade = len(dados)

        logging.info(f"Dados carregados: {quantidade} registros")

        return dados

    except FileNotFoundError:

        logging.error("Arquivo não encontrado")

        raise


# ==========================
# 2. TRATAMENTO DOS DADOS
# ==========================

def tratar_dados(dados):

    logging.info("Iniciando tratamento dos dados")

    dados["nome"] = dados["nome"].str.strip().str.title()

    dados["produto"] = dados["produto"].str.strip().str.title()

    dados["cidade"] = dados["cidade"].str.strip().str.title()

    quantidade_antes = len(dados)

    dados = dados.dropna(subset=["preco"])

    quantidade_depois = len(dados)

    quantidade_removida = quantidade_antes - quantidade_depois

    logging.info(f"Dados tratados: {quantidade_depois} registros")

    logging.info(f"Registros removidos: {quantidade_removida} registros")

    logging.info("Dados tratados com sucesso")

    return dados


# ==========================
# 3. TRANSFORMAÇÃO DOS DADOS
# ==========================

def transformar_dados(dados):

    logging.info("Iniciando transformação dos dados")

    dados["valor_com_desconto"] = np.where(
        dados["preco"] > 1000,
        dados["preco"] - (dados["preco"] * 0.1),
        dados["preco"]
    )

    logging.info("Dados transformados com sucesso")

    return dados


# ==========================
# 4. SALVAMENTO DOS DADOS
# ==========================

def salvar_dados(dados):

    logging.info("Iniciando salvamento dos dados")

    conexao = sqlite3.connect("saida/vendas.db")

    try:

        dados.to_sql(
            "vendas_tratadas",
            conexao,
            if_exists="replace",
            index=False
        )

        logging.info("Dados salvos com sucesso")

    except Exception:

        logging.error("Erro ao salvar os dados")

        raise

    finally:

        conexao.close()


# ==========================
# 5. VALIDAÇÃO DOS DADOS
# ==========================

def validar_dados(dados):

    conexao = sqlite3.connect("saida/vendas.db")

    dados_banco = pd.read_sql(
        "SELECT * FROM vendas_tratadas",
        conexao
    )

    quantidade_esperada = len(dados)

    quantidade_banco = len(dados_banco)
    
    quantidade_nulos = dados_banco.isnull().sum().sum()
    
    if quantidade_nulos == 0:
        logging.info("Validação de valores nulos: OK")
    else:
        logging.error("Validação de valores nulos: existem valores nulos")

    if quantidade_banco == quantidade_esperada:

        logging.info("Validação de quantidade: OK")

    else:

        logging.error("Validação de quantidade: registros diferentes do esperado")

    conexao.close()


# ==========================
# 6. EXECUÇÃO DO PIPELINE
# ==========================

if __name__ == "__main__":

    dados = carregar_dados()

    dados = tratar_dados(dados)

    dados = transformar_dados(dados)

    salvar_dados(dados)

    print(dados)

    validar_dados(dados)
