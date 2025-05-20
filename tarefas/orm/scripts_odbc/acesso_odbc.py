import psycopg2

# Conexão com o banco AtividadesBD
conn = psycopg2.connect(
    dbname="AtividadesBD",
    user="admin",
    password="admin123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

try:
    print("✅ Conectado ao banco com sucesso.\n")

    # a. Inserir uma nova atividade
    cur.execute("""
        INSERT INTO atividade (nome, descricao, cod_responsavel, data_inicio, data_fim)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING codigo;
    """, (
        "Análise de Requisitos ODBC",
        "Nova atividade inserida via psycopg2",
        1,  
        '2024-10-01',
        '2024-10-10'
    ))

    nova_atividade_id = cur.fetchone()[0]
    print(f"✅ Atividade inserida com id {nova_atividade_id}.")

    # b. Associar essa atividade a um projeto existente
    cur.execute("""
        INSERT INTO atividade_projeto (cod_projeto, cod_atividade)
        VALUES (%s, %s)
    """, (
        1,  
        nova_atividade_id
    ))
    print(f"✅ Atividade associada ao projeto com id 1.")

    # c. Atualizar o responsável (líder) de um projeto
    cur.execute("""
        UPDATE projeto
        SET cod_responsavel = %s
        WHERE codigo = %s;
    """, (
        2,  
        1   
    ))
    print("✅ Projeto atualizado com novo responsável.\n")

    # d. Listar todos os projetos e suas atividades
    print("📋 Projetos e suas atividades:")
    cur.execute("""
        SELECT p.nome, a.nome
        FROM projeto p
        LEFT JOIN atividade_projeto ap ON p.codigo = ap.cod_projeto
        LEFT JOIN atividade a ON a.codigo = ap.cod_atividade
        ORDER BY p.nome;
    """)

    resultados = cur.fetchall()
    for projeto_nome, atividade_nome in resultados:
        print(f"Projeto: {projeto_nome} | Atividade: {atividade_nome}")

    conn.commit()

except Exception as e:
    conn.rollback()
    print("❌ Erro durante a execução:", e)

finally:
    cur.close()
    conn.close()
    print("\n🔒 Conexão encerrada.")
