from atividades.models import Departamento, Funcionario, Projeto, Atividade, AtividadeProjeto
from datetime import date


d1 = Departamento.objects.create(descricao='TI', cod_gerente=1)
d2 = Departamento.objects.create(descricao='Financeiro', cod_gerente=2)
d3 = Departamento.objects.create(descricao='RH', cod_gerente=3)
d4 = Departamento.objects.create(descricao='Marketing', cod_gerente=4)
d5 = Departamento.objects.create(descricao='Vendas', cod_gerente=5)


f1 = Funcionario.objects.create(nome='Tony Ramos', sexo='M', dt_nasc='1985-05-10', salario=6000, cod_depto=d1)
f2 = Funcionario.objects.create(nome='Glória Pires', sexo='F', dt_nasc='1990-08-23', salario=4000, cod_depto=d2)
f3 = Funcionario.objects.create(nome='Alexandre Nero', sexo='M', dt_nasc='1987-11-14', salario=4500, cod_depto=d3)
f4 = Funcionario.objects.create(nome='Suzana Vieira', sexo='F', dt_nasc='1992-01-30', salario=5000, cod_depto=d4)
f5 = Funcionario.objects.create(nome='Ary Fontoura', sexo='M', dt_nasc='1984-04-18', salario=7000, cod_depto=d5)


p1 = Projeto.objects.create(nome='Sistema de Gestão TI', descricao='Modernização de sistemas internos', cod_depto=d1, cod_responsavel=f1, data_inicio='2023-01-01', data_fim='2023-12-31')


a1 = Atividade.objects.create(nome='Análise de Sistemas', descricao='Revisão de sistemas legados', cod_responsavel=f1, data_inicio='2023-01-01', data_fim='2023-01-15')


AtividadeProjeto.objects.create(cod_projeto=p1, cod_atividade=a1)

print("✅ Dados inseridos com sucesso.")
