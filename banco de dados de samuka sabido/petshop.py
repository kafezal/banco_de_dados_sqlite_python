import sqlite3

# Conectar ao banco de dados
banco = sqlite3.connect("petshop.db")
cursor = banco.cursor()

try:
    # CREATE: Criar a tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especie TEXT NOT NULL,
            tutor TEXT,
            idade INTEGER
        )
    """)

    print("Tabela criada com sucesso!")

    # CREATE: Cadastrar 5 pets
    cursor.execute("""
        INSERT INTO pets (nome, especie, tutor, idade)
        VALUES
        ('Nina', 'Cachorro', 'Davis', 6),
            ('Nino', 'Gato', 'Wanessa', 1),
            ('Bela', 'Coelho', 'Ana', 1),
            ('Louro', 'Papagaio', 'Antonia', 9),
            ('Nazaré', 'Peixe', 'Maria', 3)
    """)

    banco.commit()
    print("\n5 pets cadastrados com sucesso!")

    # READ: Listar todos os pets
    print("\n--- TODOS OS PETS ---")

    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()

    for pet in pets:
        print(pet)

    # READ: Listar apenas os cachorros
    print("\n--- APENAS CACHORROS ---")

    cursor.execute("""
        SELECT * FROM pets
        WHERE especie = 'Cachorro'
    """)

    cachorros = cursor.fetchall()

    for cachorro in cachorros:
        print(cachorro)

    # UPDATE: Atualizar o tutor de um pet
    cursor.execute("""
        UPDATE pets
        SET tutor = 'Diogo'
        WHERE nome = 'Nina'
    """)

    banco.commit()
    print("\nTutor atualizado com sucesso!")

    # DELETE: Excluir um pet
    cursor.execute("""
        DELETE FROM pets
        WHERE nome = 'Nina'
    """)

    banco.commit()
    print("\nPet excluído com sucesso!")

    # EXTRA: Mostrar apenas nome e tutor
    print("\n--- NOME E TUTOR DOS PETS ---")

    cursor.execute("""
        SELECT nome, tutor FROM pets
    """)

    resultado = cursor.fetchall()

    for pet in resultado:
        print("Nome:", pet[0], "| Tutor:", pet[1])

finally:
    banco.close()
    print("\nConexão com o banco encerrada!")
    