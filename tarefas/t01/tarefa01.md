# Tarefa 01 – Consultas Aninhadas, Visões e CTEs

## Scripts para resolução da lista de exercício

- [Script de criação do esquema relacional](tarefa01-create.sql)
- [Script de povoamento do esquema relacional](tarefa01-inserts.sql)
- [Script de consulta da questão 1 da lista](tarefa01-q01.sql)
- [Script de consulta da questão 4 da lista](tarefa01-q02.sql)
- [Script de consulta da questão 10 da lista](tarefa01-q03.sql)
- [Script de consulta da questão 13 da lista](tarefa01-q04.sql)
- [Script de consulta da questão 17 da lista](tarefa01-q05.sql)

---

## Questão 6

### NATURAL JOIN

O NATURAL JOIN realiza automaticamente a junção entre duas tabelas usando todas as colunas com nomes iguais em ambas as tabelas. Isso pode ser útil para simplificar a consulta, mas também pode ser perigoso se existirem colunas com o mesmo nome que não deveriam ser comparadas.

**Exemplo:**

```sql
SELECT *
FROM funcionario
NATURAL JOIN departamento;
```

Nesse exemplo, se ambas as tabelas tiverem a coluna cod_depto, ela será usada automaticamente para o JOIN.

---

## Questão 7

### Window Functions no PostgreSQL

As Window Functions (ou funções de janela) permitem realizar cálculos que levam em consideração um "conjunto de linhas" relacionadas à linha atual sem colapsar os resultados como acontece em funções de agregação comuns (SUM, AVG, etc.).

São úteis para calcular médias móveis, rankings, somatórios acumulados, entre outros.

**Exemplo:**

```sql
SELECT 
    nome,
    salario,
    AVG(salario) OVER (PARTITION BY cod_depto) AS media_salarial_departamento
FROM funcionario;
```

Esse exemplo calcula a média salarial por departamento, mantendo o detalhe de cada funcionário.
