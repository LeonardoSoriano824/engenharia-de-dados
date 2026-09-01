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
    "id": [1, 2, 3, 4, 5],
    "nome": ["Leonardo", "Carlos", "Ana", "Marina", "João"],
    "idade": [23, 27, 28, 31, 22],
    "cidade": ["Salvador", "Salvador", "Recife", "São Paulo", "Salvador"]
})

vendas = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "cliente_id": [1, 2, 1, 3, 4],
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor", "Fone"],
    "preco": [3500, 100, 250, 1200, 300]
})


# ==========================
# 3. SALVANDO OS DADOS
# ==========================

clientes.to_sql(
    "clientes",
    conexao,
    if_exists="replace",
    index=False
)

vendas.to_sql(
    "vendas",
    conexao,
    if_exists="replace",
    index=False
)


# ==========================
# 4. CONSULTA SQL
# ==========================

resultado = pd.read_sql(
    """
    SELECT
        clientes.cidade,
        SUM(vendas.preco) AS faturamento
    FROM clientes
    LEFT JOIN vendas
        ON clientes.id = vendas.cliente_id
    WHERE vendas.preco > 200
    GROUP BY clientes.cidade
    HAVING faturamento > 1000
    ORDER BY faturamento DESC
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