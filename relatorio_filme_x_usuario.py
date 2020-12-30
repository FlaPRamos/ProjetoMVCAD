# Arquivo Python que gera relatório com todos os filmes assistidos por um usuário

from psycopg_connection import cursor

def retorna_relatorio_filme_x_usuario(id):
    cursor.execute("SELECT * FROM assiste_filme, filme WHERE assiste_filme.id_filme = filme.id_filme and id_usuario = %s", [id])
    filme_x_usuario = cursor.fetchone()
    return filme_x_usuario