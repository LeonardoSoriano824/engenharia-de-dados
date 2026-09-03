import sqlite3


# ==========================================
# CONEXÃO COM O BANCO
# ==========================================

conexao = sqlite3.connect("clientes.db")

cursor = conexao.cursor()


# ==========================================
# CRIAÇÃO DA TABELA
# ==========================================

cursor.execute(
    "CREATE TABLE IF NOT EXISTS clientes ("
    "id INTEGER PRIMARY KEY, "
    "nome TEXT, "
    "idade INTEGER)"
)

conexao.commit()


# ==========================================
# INSERÇÃO DE DADOS
# ==========================================

cursor.execute(
    "INSERT INTO clientes (id, nome, idade) "
    "VALUES (2, 'Carlos', 30)"
)

conexao.commit()


# ==========================================
# CONSULTA DE DADOS
# ==========================================

cursor.execute(
    "SELECT * FROM clientes WHERE nome = 'Carlos'"
)

resultado = cursor.fetchall()

print(resultado)


# ==========================================
# ATUALIZAÇÃO DE DADOS
# ==========================================

cursor.execute(
    "UPDATE clientes "
    "SET idade = 31 "
    "WHERE nome = 'Carlos'"
)

conexao.commit()


# ==========================================
# CONSULTA APÓS ATUALIZAÇÃO
# ==========================================

cursor.execute(
    "SELECT * FROM clientes WHERE nome = 'Carlos'"
)

resultado = cursor.fetchall()

print(resultado)


# ==========================================
# EXCLUSÃO DE DADOS
# ==========================================

cursor.execute(
    "DELETE FROM clientes WHERE id = 2"
)

conexao.commit()


# ==========================================
# VERIFICAÇÃO APÓS EXCLUSÃO
# ==========================================

cursor.execute(
    "SELECT * FROM clientes WHERE id = 2"
)

resultado = cursor.fetchall()

print(resultado)


# ==========================================
# FECHAMENTO DO BANCO
# ==========================================

conexao.close()
