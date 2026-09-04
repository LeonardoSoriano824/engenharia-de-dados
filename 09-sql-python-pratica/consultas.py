import sqlite3


# ==========================================
# CONEXÃO COM O BANCO
# ==========================================

conexao = sqlite3.connect("clientes.db")

cursor = conexao.cursor()


# ==========================================
# CRIAÇÃO DA TABELA
# ==========================================

cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    cidade TEXT)''')

conexao.commit()


# ==========================================
# INSERÇÃO DOS DADOS
# ==========================================

# Os INSERTs foram executados uma vez durante a prática.
# Permanecem comentados para evitar duplicação dos registros
# ao executar o arquivo novamente.

# cursor.execute('''INSERT INTO clientes (nome, idade, cidade) 
#                VALUES ('Leonardo', 25, 'Salvador')''')

# cursor.execute('''INSERT INTO clientes (nome, idade, cidade) 
#                VALUES ('Carlos', 30, 'Recife')''')

# cursor.execute('''INSERT INTO clientes (nome, idade, cidade) 
#                VALUES ('Ana', 22, 'Salvador')''')

conexao.commit()


# ==========================================
# CONSULTA SQL
# ==========================================

dados = cursor.execute('''
    SELECT nome, idade
    FROM clientes
    ORDER BY idade DESC
''').fetchall()


# ==========================================
# PROCESSAMENTO DOS RESULTADOS COM PYTHON
# ==========================================

contador = 0

for cliente in dados:

    if cliente[1] >= 25:
        print(
            f"{cliente[0]} tem {cliente[1]} anos - "
            f"maior ou igual a 25."
        )

        contador += 1

    else:
        print(
            f"{cliente[0]} tem {cliente[1]} anos - "
            f"menor que 25."
        )


# ==========================================
# RESULTADO DA ANÁLISE
# ==========================================

print(f"Clientes com 25 anos ou mais: {contador}")