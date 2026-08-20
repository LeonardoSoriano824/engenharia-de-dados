-- WHERE
SELECT * FROM clientes WHERE idade >= 25;

-- ORDER BY
SELECT nome, idade
FROM clientes
ORDER BY idade DESC;

-- GROUP BY
SELECT cidade, COUNT(*)
FROM clientes
GROUP BY cidade;

-- HAVING
SELECT cidade, COUNT(*)
FROM clientes
GROUP BY cidade
HAVING COUNT(*) >= 2;

-- INNER JOIN
SELECT nome, produto
FROM clientes
JOIN vendas
ON clientes.id = vendas.cliente_id;

-- LEFT JOIN
SELECT nome, produto
FROM clientes
LEFT JOIN vendas
ON clientes.id = vendas.cliente_id;

-- Clientes sem compras
SELECT clientes.nome
FROM clientes
LEFT JOIN vendas
ON clientes.id = vendas.cliente_id
WHERE vendas.id IS NULL;

-- Total gasto por cliente
SELECT
    nome,
    SUM(preco) AS total_gasto
FROM clientes
JOIN vendas
ON clientes.id = vendas.cliente_id
GROUP BY nome;

-- Clientes que gastaram mais de 1000
SELECT
    nome,
    SUM(preco) AS total_gasto
FROM clientes
JOIN vendas
ON clientes.id = vendas.cliente_id
GROUP BY nome
HAVING total_gasto > 1000
ORDER BY total_gasto DESC;