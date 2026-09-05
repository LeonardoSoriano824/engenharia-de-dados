import sqlite3


# ==========================================
# CONEXÃO COM O BANCO
# ==========================================

conexao = sqlite3.connect("clientes.db")

cursor = conexao.cursor()


# ==========================================
# CRIAÇÃO DA TABELA
# ==========================================

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        cidade TEXT
    )
''')

conexao.commit()


# ==========================================
# INSERÇÃO DOS DADOS
# ==========================================

# Os INSERTs foram executados uma vez durante a prática.
# Permanecem comentados para evitar duplicação dos registros.

# cursor.execute('''
#     INSERT INTO clientes (nome, idade, cidade)
#     VALUES ('Leonardo', 25, 'Salvador')
# ''')

# cursor.execute('''
#     INSERT INTO clientes (nome, idade, cidade)
#     VALUES ('Carlos', 30, 'Recife')
# ''')

# cursor.execute('''
#     INSERT INTO clientes (nome, idade, cidade)
#     VALUES ('Ana', 22, 'Salvador')
# ''')

# cursor.execute('''
#     INSERT INTO clientes (nome, idade, cidade)
#     VALUES ('Marina', 28, 'Salvador')
# ''')

# cursor.execute('''
#     INSERT INTO clientes (nome, idade, cidade)
#     VALUES ('João', 35, 'Recife')
# ''')

# conexao.commit()


# ==========================================
# CONTAGEM TOTAL DE CLIENTES
# ==========================================

dados = cursor.execute('''
    SELECT COUNT(*)
    FROM clientes
''').fetchone()

print(f"Total de clientes: {dados[0]}")


# ==========================================
# CLIENTES POR CIDADE
# ==========================================

dados = cursor.execute('''
    SELECT cidade, COUNT(*)
    FROM clientes
    GROUP BY cidade
''').fetchall()

for cidade in dados:
    print(f"{cidade[0]} possui {cidade[1]} clientes.")


# ==========================================
# IDADE MÉDIA POR CIDADE
# ==========================================

dados = cursor.execute('''
    SELECT cidade, AVG(idade) AS idade_media
    FROM clientes
    GROUP BY cidade
''').fetchall()

for cidade in dados:
    print(f"{cidade[0]} possui idade média de {cidade[1]} anos.")


# ==========================================
# MENOR E MAIOR IDADE
# ==========================================

dados = cursor.execute('''
    SELECT MIN(idade), MAX(idade)
    FROM clientes
''').fetchone()

print(f"Menor idade: {dados[0]}")
print(f"Maior idade: {dados[1]}")


# ==========================================
# CIDADES COM PELO MENOS 3 CLIENTES
# ==========================================

dados = cursor.execute('''
    SELECT cidade, COUNT(*)
    FROM clientes
    GROUP BY cidade
    HAVING COUNT(*) >= 3
''').fetchall()

for cidade in dados:
    print(f"{cidade[0]} possui {cidade[1]} clientes.")


# ==========================================
# ANÁLISE FINAL
# ==========================================

dados = cursor.execute('''
    SELECT cidade, COUNT(*), AVG(idade) AS idade_media
    FROM clientes
    GROUP BY cidade
    HAVING COUNT(*) >= 2
''').fetchall()

for cidade in dados:
    print(
        f"{cidade[0]} possui {cidade[1]} clientes "
        f"e idade média de {cidade[2]} anos."
    )


# ==========================================
# FECHAMENTO
# ==========================================

conexao.close()