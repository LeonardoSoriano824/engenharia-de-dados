import sqlite3
import pandas as pd


# ==========================
# 1. CONEXÃO COM O BANCO
# ==========================

conexao = sqlite3.connect("clientes.db")


# ==========================
# 2. CRIAÇÃO DOS DADOS
# ==========================

clientes = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nome": ["Leonardo", "Carlos", "Ana", "Marina"],
    "idade": [23, 27, 28, 31],
    "cidade": ["Salvador", "Salvador", "Recife", "São Paulo"]
})


# ==========================
# 3. SALVANDO OS DADOS NO SQLITE
# ==========================

clientes.to_sql(
    "clientes",
    conexao,
    if_exists="replace",
    index=False
)


# ==========================
# 4. CONSULTA SQL
# ==========================

resultado = pd.read_sql(
    """
    SELECT cidade, COUNT(*) AS quantidade
    FROM clientes
    GROUP BY cidade
    ORDER BY quantidade DESC
    LIMIT 1
    """,
    conexao
)


# ==========================
# 5. EXIBINDO O RESULTADO
# ==========================

print(resultado)


# ==========================
# 6. ENCERRANDO A CONEXÃO
# ==========================

conexao.close()