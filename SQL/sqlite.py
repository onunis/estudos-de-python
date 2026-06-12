import sqlite3

nome = "Guilherme"
idade = 22
email = "guigui@gmail.com"


banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+",'"+email+"')")

banco.commit()

# cursor.execute("SELECT * FROM pessoas")
# print(cursor.fetchall())