import logging

from banco import (
    conectar_banco,
    criar_tabela,
    extrair_dados,
    transformar_dados,
    validar_dados,
    limpar_banco,
    carregar_no_banco,
    fechar_banco
)


# ==========================================
# CONFIGURAÇÃO DO LOG
# ==========================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ==========================================
# EXECUÇÃO DO PIPELINE ETL
# ==========================================

logger.info("Pipeline iniciado!")

conexao = conectar_banco()

try:

    criar_tabela(conexao)

    dados = extrair_dados()

    dados = transformar_dados(dados)

    validar_dados(dados)

    limpar_banco(conexao)

    carregar_no_banco(conexao, dados)

    logger.info("Pipeline executado com sucesso!")

except ValueError as erro:

    logger.error(f"Erro na validação: {erro}")

finally:

    fechar_banco(conexao)