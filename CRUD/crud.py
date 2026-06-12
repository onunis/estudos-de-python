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