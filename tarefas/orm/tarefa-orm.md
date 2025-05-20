# Tarefa ORM e ODBC

## Links dos scripts e programas

- [Script de acesso via ODBC com Python](./scripts_odbc/acesso_odbc.py)
- [Projeto Django com ORM](./django_orm/)
- [Modelos Django ORM](./django_orm/projeto_orm/atividades/models.py)
- [Script para carga de dados via ORM](./django_orm/load_exemplos.py)
- [Script com comandos ORM (inserir, atualizar, listar)](./django_orm/scripts.py)

---

## ODBC com Python

ODBC (Open Database Connectivity) é uma API padrão que permite que aplicações se conectem a diferentes sistemas gerenciadores de banco de dados de forma independente da linguagem ou do banco. No Python, pode ser utilizado o driver `psycopg2` para estabelecer a conexão com o PostgreSQL via ODBC/JDBC, permitindo executar comandos SQL diretamente no banco.

---

## ORM com Django

ORM (Object-Relational Mapping) é uma técnica que permite trabalhar com bancos relacionais utilizando objetos na linguagem de programação, facilitando a manipulação dos dados e abstraindo comandos SQL. Para esta tarefa, foi utilizado o framework Django, que possui um ORM integrado e poderoso. Com ele, são definidos modelos que representam as tabelas do banco, e utiliza-se métodos como `.create()`, `.save()` e `.all()` para executar operações no banco de dados PostgreSQL de maneira orientada a objetos.

---

## Referência

Esta tarefa está vinculada à issue #2
