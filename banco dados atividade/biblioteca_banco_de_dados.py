import sqlite3

# CRIANDO O BANCO DE DADOS
banco = sqlite3.connect("biblioteca.py")
cursor = banco.cursor()

# criando um tabela: livros
cursor.execute("CREATE TABLE livros(id PRIMARY KEY AUTO INCREMENT, titulo TEXT NOT NULL, autor TEXT, ano INTEGER, disponivel INTEGER)")

# inserindo os valores na tabela livros
cursor.execute("INSERT INTO livros VALUES('A Menina que Roubava Livro', 'Markus Zusak, 2005, 1)")
cursor.execute("INSERT INTO livros VALUES('Crepúsculo', 'Stephenie Meyer', 2005, 1)")
cursor.execute("INSERT INTO livros VALUES('Jogos Vorazes', 'Suzanne Collins', 2008, 1)")
cursor.execute("INSERT INTO livros VALUES('Harry Potter e o Cálice de Fogo', 'J. K. Rowling', 2000, 0)")
cursor.execute("INSERT INTO livros VALUES('Percy Jackson e o Ladrão de Raios', 'Rick Riordan', 2005, 0)")

