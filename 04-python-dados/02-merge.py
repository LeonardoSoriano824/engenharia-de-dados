import pandas as pd


# ==========================
# 1. LEITURA DOS DADOS
# ==========================

clientes = pd.read_csv("clientes.csv")
vendas = pd.read_csv("vendas.csv")


# ==========================
# 2. LIMPEZA DOS DADOS
# ==========================

clientes["cidade"] = clientes["cidade"].str.title()


# ==========================
# 3. JUNÇÃO DOS DADOS
# ==========================

dados = clientes.merge(
    vendas,
    left_on="id",
    right_on="cliente_id"
)


# ==========================
# 4. GASTOS POR CLIENTE
# ==========================

gastos_clientes = (
    dados.groupby("nome")["preco"]
    .sum()
    .reset_index()
)

gastos_clientes = gastos_clientes.rename(
    columns={"preco": "total_gasto"}
)


# ==========================
# 5. FILTRO DE CLIENTES
# ==========================

clientes_acima_1000 = (
    gastos_clientes[
        gastos_clientes["total_gasto"] >= 1000
    ]
)


# ==========================
# 6. VISUALIZAÇÃO
# ==========================

print(clientes_acima_1000)


# ==========================
# 7. FATURAMENTO POR CIDADE
# ==========================

gastos_cidades = (
    dados.groupby("cidade")["preco"]
    .sum()
    .reset_index()
)

gastos_cidades = gastos_cidades.rename(
    columns={"preco": "total_gasto"}
)


# ==========================
# 8. ORDENAÇÃO
# ==========================

gastos_cidades = gastos_cidades.sort_values(
    "total_gasto",
    ascending=False
)


# ==========================
# 9. VISUALIZAÇÃO
# ==========================

print(gastos_cidades)