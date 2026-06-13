import sqlite3

def init_db():
    with sqlite3.connect("filmes.db") as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS filmes (
                    id_filme INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    assistido INTEGER NOT NULL DEFAULT 0
                )""")

def adicionar_filme(titulo, genero):
    with sqlite3.connect("filmes.db") as conn:
        conn.execute("INSERT INTO filmes (titulo, genero) VALUES (?, ?)",(titulo, genero))

def listar_todos():
    with sqlite3.connect("filmes.db") as conn:
        return conn.execute("SELECT * FROM filmes").fetchall()

def marcar_assistido(id_filme):
    with sqlite3.connect("filmes.db") as conn:
        conn.execute("""UPDATE filmes 
                     SET assistido = 1 
                     WHERE id_filme = ?""",(id_filme,))

def listar_nao_assistidos():
    with sqlite3.connect("filmes.db") as conn:
        return conn.execute("""SELECT * FROM filmes
                            WHERE assistido = 0""").fetchall()
    
def deletar(id_filme):
    with sqlite3.connect("filmes.db") as conn:
        conn.execute("DELETE FROM filmes WHERE id_filme = ?",(id_filme,))

def menu():
    init_db()

    while True:
        print("\n--------------------------------------")
        print("1 - Adicionar Filme Novo: ")
        print("2 - Listar Todos os Filmes: ")
        print("3 - Marcar como Assistido: ")
        print("4 - Listar nao Assistidos: ")
        print("5 - Deletar da lista")
        print("0 - Sair")
        print("\n--------------------------------------")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            titulo = input("Digite o nome do filme: ")
            genero = input("Qual o genero? ")
            adicionar_filme(titulo, genero)
            print("Filme Adicionado!\n")

        elif opcao == "2":
            lista = listar_todos()
            if not lista:
                print("\nNao ha filmes na lista.")
            else:
                for id_filme, titulo, genero, assistido in lista:
                    print(f"{id_filme} | {titulo} | {genero} | {'assistido' if assistido else 'não assistido'}")
        
        elif opcao == "3":
            lista = listar_todos()
            for id_filme, titulo, genero, assistido in lista:
                    print(f"{id_filme} | {titulo} | {genero}")
            id_filme = int(input("\nDigite o Id do filme assistido: "))
            marcar_assistido(id_filme)
            print("Filme marcado como assistido!\n")
        
        elif opcao == "4":
            lista = listar_nao_assistidos()
            if not lista:
                print("Todos os filmes já foram assistidos!")
            else:
                for id_filme, titulo, genero, assistido in lista:
                    print(f"{id_filme} | {titulo} | {genero}")
        
        elif opcao == "5":
            delete_id = input("Digite o Id do filme que voce quer deletar da lista: ")
            deletar(int(delete_id))
            print("Filme deletado da lista.\n")
        
        elif opcao == "0":
            break

menu()