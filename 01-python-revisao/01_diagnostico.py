clientes = [
    {"nome": "Leonardo", "idade": 23, "cidade": "Salvador"},
    {"nome": "Ana", "idade": 28, "cidade": "Recife"},
    {"nome": "Carlos", "idade": 19, "cidade": "Salvador"},
    {"nome": "Marina", "idade": 31, "cidade": "São Paulo"}
]

vendas = [
    {"produto": "Notebook", "preco": 3500},
    {"produto": "Mouse", "preco": 100},
    {"produto": "Teclado", "preco": 250},
    {"produto": "Monitor", "preco": 1200}
]

precos = []

cidades = []

print("Clientes:")
for cliente in clientes:
    print(cliente["nome"])
    
print("=====================================")

print("Idade >= 25:")    
for cliente in clientes:
    if cliente["idade"] >= 25:
        print(cliente["nome"])
        
print("=====================================")
print("Cidades:")    
for cliente in clientes:
    cidades.append(cliente["cidade"])

print(cidades)

print("=====================================")
print("Valor total:")    
for produto in vendas:
    precos.append(produto["preco"])
print(sum(precos))

print("=====================================")
print("Maior preço:")    
maior_preco = 0
nome_produto = ""
for produto in vendas:
    if produto["preco"] > maior_preco:
        maior_preco = produto["preco"]
        nome_produto = produto["produto"]
print(nome_produto)
print(maior_preco)