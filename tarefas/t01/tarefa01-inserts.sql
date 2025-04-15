
INSERT INTO departamento (descricao, cod_gerente) 
VALUES 
('TI', 1),
('Financeiro', 2),
('RH', 3),
('Marketing', 4),
('Vendas', 5);


INSERT INTO funcionario (nome, sexo, dt_nasc, salario, cod_depto) 
VALUES 
('Tony Ramos', 'M', '1985-05-10', 4000, 1),
('Glória Pires', 'F', '1990-08-23', 3500, 2),
('Alexandre Nero', 'M', '1987-11-14', 5000, 3),
('Suzana Vieira', 'F', '1992-01-30', 4500, 4),
('Ary Fontoura', 'M', '1984-04-18', 5500, 5);


INSERT INTO projeto (nome, descricao, cod_depto, cod_responsavel, data_inicio, data_fim) 
VALUES 
('Sistema de Gestão TI', 'Modernização de sistemas internos', 1, 1, '2023-01-01', '2023-12-31'),
('Análise Financeira', 'Revisão e ajuste financeiro', 2, 2, '2023-02-01', '2023-11-30'),
('Seleção de Talentos', 'Contratação de novos funcionários', 3, 3, '2023-03-01', '2023-10-15'),
('Campanha Publicitária', 'Reforço da marca nas redes sociais', 4, 4, '2023-04-01', '2023-09-30'),
('Expansão Comercial', 'Expansão da rede de vendas', 5, 5, '2023-05-01', '2023-08-15');


INSERT INTO atividade (nome, descricao, cod_responsavel, data_inicio, data_fim) 
VALUES 
('Análise de Sistemas', 'Revisão de sistemas legados', 1, '2023-01-01', '2023-01-15'),
('Auditoria de Contas', 'Revisão de processos financeiros', 2, '2023-02-01', '2023-02-15'),
('Entrevistas de Seleção', 'Realização de entrevistas', 3, '2023-03-01', '2023-03-15'),
('Criação de Conteúdo', 'Desenvolvimento de conteúdo digital', 4, '2023-04-01', '2023-04-15'),
('Treinamento de Equipe', 'Capacitação de novos vendedores', 5, '2023-05-01', '2023-05-15');


INSERT INTO atividade_projeto (cod_projeto, cod_atividade) 
VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);
