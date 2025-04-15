
CREATE TABLE departamento (
    codigo SERIAL PRIMARY KEY,
    descricao VARCHAR(255),
    cod_gerente INT
);


CREATE TABLE funcionario (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    sexo CHAR(1),
    dt_nasc DATE,
    salario DECIMAL(10, 2),
    cod_depto INT,
    cod_supervisor INT
);


ALTER TABLE funcionario
ADD CONSTRAINT fk_funcionario_depto FOREIGN KEY (cod_depto) REFERENCES departamento(codigo);


ALTER TABLE funcionario
ADD CONSTRAINT fk_funcionario_supervisor FOREIGN KEY (cod_supervisor) REFERENCES funcionario(codigo);


CREATE TABLE projeto (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    descricao TEXT,
    cod_depto INT,
    cod_responsavel INT,
    data_inicio DATE,
    data_fim DATE,
    FOREIGN KEY (cod_depto) REFERENCES departamento(codigo),
    FOREIGN KEY (cod_responsavel) REFERENCES funcionario(codigo)
);


CREATE TABLE atividade (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    descricao TEXT,
    cod_responsavel INT,
    data_inicio DATE,
    data_fim DATE,
    FOREIGN KEY (cod_responsavel) REFERENCES funcionario(codigo) 
);


CREATE TABLE atividade_projeto (
    cod_projeto INT,
    cod_atividade INT,
    FOREIGN KEY (cod_projeto) REFERENCES projeto(codigo),
    FOREIGN KEY (cod_atividade) REFERENCES atividade(codigo) 
);
