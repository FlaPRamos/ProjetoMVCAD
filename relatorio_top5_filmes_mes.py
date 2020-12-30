# Arquivo Python que gera relatório com o TOP5 pessoas que mais assistiram filmes no mês

from psycopg_connection import cursor

def retorna_relatorio_pessoas_filmes_mes(id):
    cursor.execute("SELECT usuario.nome FROM assiste_filme, filme, usuario WHERE assiste.filme.data >= %(data_inicial)s AND < %(data_final) AND assiste_filme.id_filme = filme.id_filme and assiste_epsidio.id_usuario = %s", [id])
    top_filmes_usuario = cursor.fetchone()
    top_usuario = [top_filmes_usuario]
    top_usuario.sort()
    top5 = top_usuario[0,4]
    return top5

