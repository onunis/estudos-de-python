import sqlite3

def init_db():
    with sqlite3.connect("gastos.db") as conn:
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
