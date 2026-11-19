import sqlite3

# CRIANDO O BANCO DE DADOS
banco = sqlite3.connect("biblioteca.db")
cursor = banco.cursor()

# criando um tabela: livros
cursor.execute("CREATE TABLE livros(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, autor TEXT, ano INTEGER, disponivel INTEGER)")

# lista dos livros
lista_livro = [
    ('A Menina que Roubava Livro', 'Markus Zusak', 2005, 1),
    ('Crepúsculo', 'Stephenie Meyer', 2005, 1),
    ('Drácula ', 'Bram Stoker ', 1897, 1),
    ('Crime e Castigo ', 'Fiódor Dostoiévski ', 1866, 0),
    ('Percy Jackson e o Ladrão de Raios', 'Rick Riordan', 2005, 0)
]

# inserindo os valores na tabela livros
cursor.executemany(
    "INSERT INTO livros (titulo, autor, ano, disponivel) VALUES (?, ?, ?, ?)",
    lista_livro
)

banco.commit()

# mostrar todos os livros
print("todos os livros")

cursor.execute("SELECT * FROM livros")
print(cursor.fetchall())

print("---" * 25)

# mostrar todo os livros disponíveis
print("livros disponíveis")

cursor.execute("SELECT titulo FROM livros WHERE disponivel = 1")
livros = cursor.fetchall()

for livro in livros:
    print(livro)

print("-" * 25)

# empréstimo de um livro (livro Crepúsculo)
print("emprestando o crepúsculo")

cursor.execute(
    "UPDATE livros SET disponivel = ? WHERE titulo = ?",
    (0, 'Crepúsculo')
)
banco.commit()

print("-" * 25)

# removendo um livro (livro Percy Jackson e o Ladrão de Raios)
print("removendo o Percy Jackson e o Ladrão de Raios")

cursor.execute("DELETE FROM livros WHERE id = ?", (5,))
banco.commit()

print("-" * 25)

# listando livros depois do ano 2000
print("todos os livros depois dos anos 2000")

cursor.execute("SELECT titulo FROM livros WHERE ano > 2000")
livros = cursor.fetchall()

for livro in livros:
    print(livro)

# fechando o banco
banco.close()