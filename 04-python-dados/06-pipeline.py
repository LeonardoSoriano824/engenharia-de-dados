import pandas as pd
import numpy as np


# ==========================
# 1. LEITURA DOS DADOS
# ==========================

clientes = pd.read_csv("clientes_sujos.csv")
vendas = pd.read_csv("vendas.csv")


# ==========================
# 2. LIMPEZA DOS DADOS
# ==========================

clientes["nome"] = clientes["nome"].str.strip().str.title()

clientes["cidade"] = clientes["cidade"].str.strip().str.title()


# ==========================
# 3. TRATAMENTO DE VALORES AUSENTES
# ==========================

clientes["idade"] = clientes["idade"].fillna(
    clientes["idade"].mean()
).astype(int)


# ==========================
# 4. CRIAÇÃO DE CATEGORIA
# ==========================

clientes["faixa_etaria"] = np.where(
    clientes["idade"] < 25,
    "Jovem",
    "Adulto"
)


# ==========================
# 5. JUNÇÃO DOS DADOS
# ==========================

dados = clientes.merge(
    vendas,
    left_on="id",
    right_on="cliente_id"
)


# ==========================
# 6. GASTOS POR CLIENTE
# ==========================

gastos_totais = (
    dados.groupby("nome")["preco"]
    .sum()
    .reset_index()
)


# ==========================
# 7. FATURAMENTO POR CIDADE
# ==========================

faturamento_cidades = (
    dados.groupby("cidade")["preco"]
    .sum()
    .reset_index()
)


# ==========================
# 8. ORDENAÇÃO
# ==========================

faturamento_cidades = faturamento_cidades.sort_values(
    "preco",
    ascending=False
)


# ==========================
# 9. VALIDAÇÃO E VISUALIZAÇÃO
# ==========================

print(clientes)
print(clientes.dtypes)

print(vendas)
print(vendas.dtypes)

print(clientes.isna().sum())
print(vendas.isna().sum())

print(dados)
print(gastos_totais)
print(faturamento_cidades)

print("clientes:", len(clientes))
print("vendas:", len(vendas))
print("dados:", len(dados))


# ==========================
# 10. EXPORTAÇÃO DO RESULTADO
# ==========================

faturamento_cidades.to_csv(
    "faturamento_cidades.csv",
    index=False
)

gastos_totais.to_csv(
    "gastos_totais_clientes.csv",
    index=False
)

