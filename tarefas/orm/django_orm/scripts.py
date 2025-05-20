from atividades.models import Projeto, Atividade, Funcionario, AtividadeProjeto
from datetime import date

# a. Inserir uma atividade em algum projeto
func = Funcionario.objects.first()
proj = Projeto.objects.first()

atividade = Atividade.objects.create(
    nome="Atividade ORM",
    descricao="Criada via ORM",
    cod_responsavel=func,
    data_inicio=date(2024, 10, 1),
    data_fim=date(2024, 10, 20)
)

AtividadeProjeto.objects.create(
    cod_projeto=proj,
    cod_atividade=atividade
)

# b. Atualizar o líder de algum projeto
novo_responsavel = Funcionario.objects.last()
proj.cod_responsavel = novo_responsavel
proj.save()

# c. Listar todos os projetos e suas atividades
print("\nProjetos e suas Atividades:")
for p in Projeto.objects.all():
    print(f"Projeto: {p.nome}")
    for ap in p.atividades_projeto.all():
        print(f"  - {ap.cod_atividade.nome}")
