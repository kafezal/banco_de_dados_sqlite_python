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
    "UPDATE boletim SET nota2 = ? WHERE id = ?",
    (3.5, '3')
)
banco.commit()

print("-" * 25)

# removendo um aluno
print("removendo um aluno")

cursor.execute("DELETE FROM boletim WHERE id = ?", (4,))
banco.commit()

print("-" * 25)

# registrando se tá passado ou não
print("Resultado final:")
cursor.execute("SELECT id, aluno, disciplina, nota1, nota2 FROM boletim")
registros = cursor.fetchall()

for id_aluno, aluno, disciplina, nota1, nota2 in registros:
    media = (nota1 + nota2) / 2
    print(f"Aluno: {aluno}")
    print(f"Disciplina: {disciplina}")
    print(f"Nota 1 = {nota1} | Nota 2 = {nota2} | Média = {media:.1f}")
    
    if media >= 6:
        print(f"Situação: {aluno} passou!\n")
    else:
        print(f"Situação: {aluno} reprovou.\n")


# fechando o banco
banco.close()
