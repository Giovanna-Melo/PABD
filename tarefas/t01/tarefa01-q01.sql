SELECT nome
FROM funcionario
WHERE salario > ANY (
    SELECT salario
    FROM funcionario
    WHERE cod_depto = 2
) AND cod_depto != 2;
