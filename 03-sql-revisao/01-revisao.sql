-- ============================================
-- REVISÃO DE SQL
-- Projeto: Engenharia de Dados
-- ============================================


-- ============================================
-- 1. WHERE
-- Filtra registros de acordo com uma condição
-- ============================================

SELECT *
FROM clientes
WHERE idade >= 25;


-- ============================================
-- 2. ORDER BY
-- Ordena os resultados
-- DESC = maior para menor
-- ASC = menor para maior
-- ============================================

SELECT nome, idade
FROM clientes
ORDER BY idade DESC;


-- ORDER BY + LIMIT
-- Retorna apenas os primeiros resultados

SELECT nome, idade
FROM clientes
ORDER BY idade DESC
LIMIT 1;


-- ============================================
-- 3. FUNÇÕES DE AGREGAÇÃO
-- COUNT, SUM, AVG, MIN e MAX
-- ============================================

-- COUNT
-- Conta registros

SELECT COUNT(*)
FROM clientes;


-- COUNT(coluna)
-- Ignora valores NULL

SELECT COUNT(nome)
FROM clientes;


-- SUM
-- Soma os valores de uma coluna

SELECT SUM(idade)
FROM clientes;


-- AVG
-- Calcula a média

SELECT AVG(idade)
FROM clientes;


-- MIN
-- Retorna o menor valor

SELECT MIN(idade)
FROM clientes;


-- MAX
-- Retorna o maior valor

SELECT MAX(idade)
FROM clientes;


-- ============================================
-- 4. WHERE + FUNÇÕES DE AGREGAÇÃO
-- ============================================

-- Média de idade dos clientes de Salvador

SELECT AVG(idade)
FROM clientes
WHERE cidade = 'Salvador';


-- Maior idade entre os clientes de Salvador

SELECT MAX(idade)
FROM clientes
WHERE cidade = 'Salvador';


-- ============================================
-- 5. GROUP BY
-- Agrupa registros por uma coluna
-- ============================================

SELECT cidade, COUNT(*)
FROM clientes
GROUP BY cidade;


-- Média de idade por cidade

SELECT cidade, AVG(idade)
FROM clientes
GROUP BY cidade;


-- ============================================
-- 6. HAVING
-- Filtra grupos depois do GROUP BY
-- ============================================

-- Cidades com pelo menos 2 clientes

SELECT cidade, COUNT(*)
FROM clientes
GROUP BY cidade
HAVING COUNT(*) >= 2;


-- Cidades com pelo menos 2 clientes,
-- ordenadas pela média de idade

SELECT cidade, AVG(idade)
FROM clientes
GROUP BY cidade
HAVING COUNT(*) >= 2
ORDER BY AVG(idade) DESC;


-- ============================================
-- 7. INNER JOIN
-- Retorna somente registros que possuem
-- correspondência nas duas tabelas
-- ============================================

SELECT nome, produto
FROM clientes
JOIN vendas
ON clientes.id = vendas.cliente_id;


-- ============================================
-- 8. LEFT JOIN
-- Mantém todos os registros da tabela da esquerda,
-- mesmo que não exista correspondência na direita
-- ============================================

SELECT nome, produto
FROM clientes
LEFT JOIN vendas
ON clientes.id = vendas.cliente_id;


-- ============================================
-- 9. NULL
-- Para verificar NULL usamos IS NULL
-- e IS NOT NULL.
-- Não usamos = NULL.
-- ============================================

-- Clientes sem compras

SELECT clientes.nome
FROM clientes
LEFT JOIN vendas
ON clientes.id = vendas.cliente_id
WHERE vendas.id IS NULL;


-- ============================================
-- 10. COALESCE
-- Substitui NULL por outro valor
-- ============================================

-- Total gasto por todos os clientes,
-- incluindo quem não realizou compras

SELECT
    nome,
    COALESCE(SUM(preco), 0) AS total_gasto
FROM clientes
LEFT JOIN vendas
ON clientes.id = vendas.cliente_id
GROUP BY nome;


-- ============================================
-- 11. SUM + JOIN + GROUP BY
-- Total gasto por cliente
-- ============================================

SELECT
    nome,
    SUM(preco) AS total_gasto
FROM clientes
JOIN vendas
ON clientes.id = vendas.cliente_id
GROUP BY nome;


-- ============================================
-- 12. HAVING + SUM
-- Clientes que gastaram mais de R$ 1.000
-- ============================================

SELECT
    nome,
    SUM(preco) AS total_gasto
FROM clientes
JOIN vendas
ON clientes.id = vendas.cliente_id
GROUP BY nome
HAVING total_gasto > 1000
ORDER BY total_gasto DESC;


-- ============================================
-- 13. SUBQUERY
-- Consulta dentro de outra consulta
-- ============================================

-- Clientes com idade acima da média

SELECT nome, idade
FROM clientes
WHERE idade > (
    SELECT AVG(idade)
    FROM clientes
);


-- ============================================
-- 14. SUBQUERY COM AGREGAÇÃO
-- Produtos com preço acima da média
-- ============================================

SELECT produto, preco
FROM vendas
WHERE preco > (
    SELECT AVG(preco)
    FROM vendas
);


-- ============================================
-- 15. IN + SUBQUERY
-- IN verifica se um valor pertence
-- aos resultados de uma lista
-- ============================================

-- Clientes que moram em cidades
-- com mais de um cliente

SELECT nome
FROM clientes
WHERE cidade IN (
    SELECT cidade
    FROM clientes
    GROUP BY cidade
    HAVING COUNT(*) > 1
);


-- ============================================
-- 16. NOT IN + SUBQUERY
-- NOT IN exclui valores que pertencem
-- aos resultados da subquery
-- ============================================

-- Clientes que não moram em cidades
-- com mais de um cliente

SELECT nome
FROM clientes
WHERE cidade NOT IN (
    SELECT cidade
    FROM clientes
    GROUP BY cidade
    HAVING COUNT(*) > 1
);


-- ============================================
-- 17. CTE (Common Table Expression)
-- WITH cria um resultado temporário
-- que pode ser usado pela consulta principal
-- ============================================

-- Clientes com idade maior ou igual a 25

WITH clientes_maiores AS (
    SELECT nome, idade
    FROM clientes
    WHERE idade >= 25
)
SELECT nome
FROM clientes_maiores;


-- ============================================
-- 18. CTE + JOIN + SUM + COALESCE
-- Total gasto por todos os clientes,
-- incluindo quem não comprou
-- ============================================

WITH gastos_clientes AS (
    SELECT
        nome,
        cidade,
        COALESCE(SUM(preco), 0) AS total_gasto
    FROM clientes
    LEFT JOIN vendas
        ON clientes.id = vendas.cliente_id
    GROUP BY nome, cidade
)
SELECT *
FROM gastos_clientes;


-- ============================================
-- FIM DA REVISÃO ATUAL
-- ============================================