import sqlite3

# CRIANDO O BANCO DE DADOS
banco = sqlite3.connect("notas.db")
cursor = banco.cursor()

# criando um tabela: boletim
cursor.execute("CREATE TABLE boletim(id INTEGER PRIMARY KEY AUTOINCREMENT, aluno TEXT NOT NULL, disciplina TEXT, nota1 REAL, nota2 REAL)")

# lista dos boletim
lista_boletim = [
    ('joão bonifácio', 'inglês', 5.5, 9),
    ('maria bonitinha', 'matemática', 8, 10),
    ('van helsing', 'literatura ', 8.5, 6.5),
    ('matheus lutero', 'química ', 10, 10),
    ('lara silva', 'português', 5, 8)
]

# inserindo os valores na tabela boletim
cursor.executemany(
    "INSERT INTO boletim (aluno, disciplina, nota1, nota2) VALUES (?, ?, ?, ?)",
    lista_boletim
)

banco.commit()

# mostrar todos os no boletim                                                                                                                             
print("todos os alunos no boletim")

cursor.execute("SELECT * FROM boletim")
print(cursor.fetchall())

print("---" * 25)

# mudando a nota de um aluno
print("alterando a nota")

cursor.execute(
    "UPDATE boletim SET nota2 = ? WHERE nome = ?",
    (3.5, 'van helsing')
)
banco.commit()

print("-" * 25)

# removendo um aluno
print("removendo um aluno")

cursor.execute("DELETE FROM boletim WHERE id = ?", (4,))
banco.commit()

print("-" * 25)

# registrando se tá passado ou não
print("resultado")

cursor.execute("SELECT aluno FROM boletim")
alunos = cursor.fetchall()
cursor.execute("SELECT disciplina FROM boletim")
disciplinas = cursor.fetchall()
cursor.execute("SELECT nota1 FROM boletim")
notas1 = cursor.fetchall()
cursor.execute("SELECT nota2 FROM boletim")
notas2 = cursor.fetchall()

for aluno in alunos:
    print('aluno: ', aluno)


            


# fechando o banco
banco.close()