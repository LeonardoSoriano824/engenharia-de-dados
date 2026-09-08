import pandas as pd


# ==========================================
# CRIAÇÃO DOS DADOS
# ==========================================

dados = {
    "id": [1, 2, 3, 4, 5],
    "nome": ["Leonardo", "Carlos", "Ana", "Marina", "João"],
    "idade": [25, 30, 22, 28, 35],
    "cidade": ["Salvador", "Recife", "Salvador", "São Paulo", "Recife"],
    "salario": [3000, 4500, 2800, 5200, 6000]
}

df = pd.DataFrame(dados)


# ==========================================
# ORDENAÇÃO
# ==========================================

df_ordenado = df.sort_values("idade")


# ==========================================
# RENOMEAÇÃO DE COLUNA
# ==========================================

df_renomeado = df.rename(
    columns={"salario": "salario_mensal"}
)


# ==========================================
# REMOÇÃO DE COLUNA
# ==========================================

df_sem_id = df.drop(columns="id")


# ==========================================
# CRIAÇÃO DE UMA FUNÇÃO
# ==========================================

def classificar_idade(idade):

    if idade < 25:
        return "Jovem"

    else:
        return "Adulto"


# ==========================================
# APLICAÇÃO DA FUNÇÃO
# ==========================================

df["categoria"] = df["idade"].apply(classificar_idade)


# ==========================================
# CRIAÇÃO DO DATAFRAME DE COMPRAS
# ==========================================

compras = pd.DataFrame({
    "id_cliente": [1, 2, 3, 4, 5],
    "valor": [300, 500, 200, 800, 1000]
})


# ==========================================
# JUNÇÃO DE DATAFRAMES COM MERGE
# ==========================================

df_completo = df.merge(
    compras,
    left_on="id",
    right_on="id_cliente"
)


# ==========================================
# CRIAÇÃO DE UMA NOVA COLUNA
# ==========================================

df_completo["valor_total"] = (
    df_completo["salario"] +
    df_completo["valor"]
)


# ==========================================
# CONCATENAÇÃO DE DATAFRAMES
# ==========================================

clientes_janeiro = pd.DataFrame({
    "nome": ["Leonardo", "Carlos"],
    "cidade": ["Salvador", "Recife"]
})


clientes_fevereiro = pd.DataFrame({
    "nome": ["Ana", "Marina"],
    "cidade": ["Salvador", "São Paulo"]
})


df_clientes = pd.concat([
    clientes_janeiro,
    clientes_fevereiro
])


# ==========================================
# ANÁLISE DO MAIOR VALOR
# ==========================================

cliente_maior_valor = (
    df_completo
    .sort_values("valor_total", ascending=False)
    .head(1)["nome"]
    .iloc[0]
)

print(f"Cliente com maior valor total: {cliente_maior_valor}")