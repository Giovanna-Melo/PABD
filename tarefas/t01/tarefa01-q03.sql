WITH projeto_info AS (
    SELECT 
        p.nome AS nome_projeto,
        p.cod_depto AS cod_depto_projeto,
        p.cod_responsavel,
        d1.descricao AS departamento_projeto
    FROM projeto p
    JOIN departamento d1 ON p.cod_depto = d1.codigo
)
SELECT 
    pi.nome_projeto,
    pi.departamento_projeto,
    f.nome AS responsavel_projeto,
    d2.descricao AS departamento_responsavel
FROM projeto_info pi
JOIN funcionario f ON pi.cod_responsavel = f.codigo
JOIN departamento d2 ON f.cod_depto = d2.codigo;
