import sqlite3

try:
    
    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()

    cursor.execute("DELETE FROM pessoas WHERE idade = gui")

    banco.commit()
    banco.close()
    print("os dados foram removidos com sucesso!")


except sqlite3.Error as Erro:
    print("Erro ao excluir: ",Erro)