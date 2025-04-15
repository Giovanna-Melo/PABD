CREATE VIEW vw_gerentes AS
SELECT d.codigo AS cod_depto, d.cod_gerente, f.salario
FROM departamento d
JOIN funcionario f ON d.cod_gerente = f.codigo;

SELECT 
    p.codigo,
    p.descricao
FROM projeto p
JOIN vw_gerentes vg ON p.cod_depto = vg.cod_depto
WHERE vg.salario > ALL (
    SELECT salario FROM vw_gerentes WHERE cod_depto <> vg.cod_depto
);