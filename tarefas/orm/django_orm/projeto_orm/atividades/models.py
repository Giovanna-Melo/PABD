from django.db import models

class Departamento(models.Model):
    descricao = models.CharField(max_length=255)
    cod_gerente = models.IntegerField(null=True, blank=True)  # relação não definida no SQL

    def __str__(self):
        return self.descricao


class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1)
    dt_nasc = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    cod_depto = models.ForeignKey(
        Departamento, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="funcionarios"
    )
    cod_supervisor = models.ForeignKey(
        'self', on_delete=models.SET_NULL,
        null=True, blank=True, related_name="subordinados"
    )

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    cod_depto = models.ForeignKey(
        Departamento, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="projetos"
    )
    cod_responsavel = models.ForeignKey(
        Funcionario, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="projetos_que_lidera"
    )
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    cod_responsavel = models.ForeignKey(
        Funcionario, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="atividades"
    )
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome


class AtividadeProjeto(models.Model):
    cod_projeto = models.ForeignKey(
        Projeto, on_delete=models.CASCADE, related_name="atividades_projeto"
    )
    cod_atividade = models.ForeignKey(
        Atividade, on_delete=models.CASCADE, related_name="projetos_vinculados"
    )

    class Meta:
        unique_together = (('cod_projeto', 'cod_atividade'),)
