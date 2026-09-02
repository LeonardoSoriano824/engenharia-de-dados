import pandas as pd


# ==========================
# 1. REVISÃO DE ETL
# ==========================

dados = pd.DataFrame({
    "nome": [" Leonardo ", "MARIA", " joão "],
    "cidade": ["salvador", "RECIFE", " salvador "]
})

print("Dados antes da transformação:")
print(dados)

# Transformação dos dados
dados["nome"] = dados["nome"].str.strip().str.title()
dados["cidade"] = dados["cidade"].str.strip().str.title()

print("\nDados depois da transformação:")
print(dados)


# ==========================
# 2. CONSULTAS SQL — SELECT E WHERE
# ==========================

# SELECT nome, preco
# FROM vendas;

# SELECT nome, preco
# FROM vendas
# WHERE preco > 1000;


# ==========================
# 3. ORDER BY
# ==========================

# SELECT nome, preco
# FROM vendas
# ORDER BY preco DESC;


# ==========================
# 4. WHERE + ORDER BY
# ==========================

# SELECT nome, preco
# FROM vendas
# WHERE cidade = 'Salvador'
# ORDER BY preco DESC;


# ==========================
# 5. GROUP BY + COUNT
# ==========================

# SELECT cidade, COUNT(*) AS vendas_cidade
# FROM vendas
# GROUP BY cidade;


# ==========================
# 6. GROUP BY + HAVING
# ==========================

# SELECT cidade, COUNT(*) AS vendas_cidade
# FROM vendas
# GROUP BY cidade
# HAVING COUNT(*) >= 2;


# ==========================
# 7. WHERE + GROUP BY + HAVING
# ==========================

# SELECT cidade, COUNT(*) AS vendas_cidade
# FROM vendas
# WHERE preco > 500
# GROUP BY cidade
# HAVING COUNT(*) >= 2;


# ==========================
# 8. FUNÇÕES DE AGREGAÇÃO
# ==========================

# SELECT SUM(preco)
# FROM vendas;

# SELECT AVG(preco)
# FROM vendas;

# SELECT MAX(preco)
# FROM vendas;

# SELECT MIN(preco)
# FROM vendas;

# SELECT COUNT(*)
# FROM vendas;


# ==========================
# 9. AVG + WHERE
# ==========================

# SELECT AVG(preco) AS preco_medio
# FROM vendas
# WHERE cidade = 'Salvador';


# ==========================
# 10. GROUP BY + AVG + HAVING
# ==========================

# SELECT cidade, AVG(preco) AS preco_medio
# FROM vendas
# GROUP BY cidade
# HAVING AVG(preco) > 500;