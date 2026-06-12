import sqlite3

def init_db():
    with sqlite3.connect("crud.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
                nome         TEXT    NOT NULL
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS gastos (
                id_gasto     INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao    TEXT    NOT NULL,
                valor        REAL    NOT NULL,
                data         TEXT    NOT NULL,
                id_categoria INTEGER NOT NULL,
                FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
            )
        """)

def adicionar_categoria(nome):
    with sqlite3.connect("crud.db") as conn:
        conn.execute("INSERT INTO categorias (nome) VALUES (?)",(nome,))

def listar_categorias():
    with sqlite3.connect("crud.db") as conn:
        return conn.execute(
            "SELECT * FROM categorias"
        ).fetchall()

def adicionar_gasto(descricao, valor, data, id_categoria):
    with sqlite3.connect("crud.db") as conn:
        conn.execute("INSERT INTO gastos (descricao, valor, data, id_categoria) VALUES (?,?,?,?)",(descricao,valor,data, id_categoria))

def listar_gastos():
    with sqlite3.connect("crud.db") as conn:
        return conn.execute(
            "SELECT * FROM gastos"
        ).fetchall()
    
def deletar_gasto(id_gasto):
    with sqlite3.connect("crud.db") as conn:
        conn.execute("DELETE FROM gastos WHERE (id_gasto) = (?)",(id_gasto,))

def total_categoria():
    with sqlite3.connect("crud.db") as conn:
        return conn.execute("""SELECT categorias.nome, SUM(gastos.valor)
                     FROM gastos
                     INNER JOIN categorias ON gastos.id_categoria = categorias.id_categoria
                     GROUP BY categorias.nome
    """).fetchall()


def menu():
    init_db()

    while True:
        print("\n1 - Adicionar Categorias")
        print("\n2 - Listar Categorias")
        print("\n3 - Adicionar Gastos")
        print("\n4 - Listar Gastos")
        print("\n5 - Deletar Gastos")
        print("\n6 - Total por Categoria")
        print("\n0 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            nome = input("\nNome da categoria: ")
            adicionar_categoria(nome)
            print("\ncategoria adicionada!")

        elif opcao == "2":
            categorias = listar_categorias()
            if not categorias:
                print("\nNenhuma categoria encontrada.")
            else:
                for id, nome in categorias:
                    print(f"{id} | {nome}")

        elif opcao == "3":
            descricao = input("\nDescreva o gasto: ")
            valor = int(input("\nQuanto foi gasto: "))
            data = input("\nQuando foi feito esse gasto? ")
            id_categoria = int(input("\nDigite o Id da categoria desejada: "))
            adicionar_gasto(descricao, valor, data, id_categoria)

        elif opcao == "4":
            gastos = listar_gastos()
            if not gastos:
                print("\nNenhum gasto encontrado. Parabens!")
            else:
                for id, descricao, valor, data, id_categoria in gastos:
                    print(f"{id} | {descricao} | R$:{valor} | {data} | cat:{id_categoria}")

        elif opcao == "5":
            delete_id = input("\nDigite o Id do Gasto que voce quer deletar: ")
            deletar_gasto(int(delete_id))
            print("Id Deletado. ")
        
        elif opcao == "6":
            totais = total_categoria()
            for nome, total in totais:
                print(f"{nome} -> R${total:.2f}") 

        elif opcao == "0":
            break


menu()