# -- CRUD filme

from psycopg_connection import cursor

def insere_filme(dados_filme):

    cursor.execute("INSERT INTO filme (nome, descricao, baseado_em, classificacao, genero, elenco, duracao, idioma, ano_lancamento, pais_origem)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (
                       dados_filme['nome'],
                       dados_filme['descricao'],
                       dados_filme['baseado_em'],
                       dados_filme['classificacao'],
                       dados_filme['genero'],
                       dados_filme['elenco'],
                       dados_filme['duracao'],
                       dados_filme['idioma'],
                       dados_filme['ano_lancamento'],
                       dados_filme['pais_origem']
                   )
                   )


def retorna_filmes():
    cursor.execute("SELECT * FROM filme")
    return cursor.fetchall()


def retorna_filme(id):

    cursor.execute("SELECT * FROM filme WHERE id_filme = %s", [id])
    filme = cursor.fetchone()
    return filme


def atualiza_filme(filme):
    query = "UPDATE filme SET nome = %s, descricao = %s, baseado_em = %s, classificacao = %s, genero = %s, elenco = %s, duracao = %s, idioma = %s, ano_lancamento = %s, pais_origem = %s" \
            "WHERE id_filme = %s"
    params = [filme['nome'], filme['descricao'], filme['baseado_em'], filme['classificacao'], filme['genero'], filme['elenco'],
              filme['duracao'], filme['idioma'], filme['ano_lancamento'], filme['pais_origem'], filme['id_filme']]

    cursor.execute(query, params)

def remove_filme(id):
    cursor.execute("DELETE FROM filme WHERE id_filme = %s", [id])