import pandas as pd
import numpy as np


# ==========================
# 1. LEITURA DOS DADOS
# ==========================

vendas = pd.read_csv("vendas.csv")


# ==========================
# 2. CRIAÇÃO DA QUANTIDADE
# ==========================

vendas["quantidade"] = [2, 3, 5, 1, 4]


# ==========================
# 3. CÁLCULO DO VALOR TOTAL
# ==========================

vendas["valor_total"] = (
    vendas["quantidade"] * vendas["preco"]
)


# ==========================
# 4. CLASSIFICAÇÃO DAS VENDAS
# ==========================

vendas["categoria"] = np.where(
    vendas["valor_total"] >= 1000,
    "Alta",
    "Baixa"
)


# ==========================
# 5. CÁLCULO DO DESCONTO
# ==========================

vendas["desconto"] = np.where(
    vendas["valor_total"] >= 1000,
    0.10,
    0
)


# ==========================
# 6. CÁLCULO DO VALOR FINAL
# ==========================

vendas["valor_final"] = (
    vendas["valor_total"] * (1 - vendas["desconto"])
)


# ==========================
# 7. VISUALIZAÇÃO
# ==========================

print(vendas)