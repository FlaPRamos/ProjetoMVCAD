# -- CRUD serie

from psycopg_connection import cursor

def insere_serie(dados_serie):

    cursor.execute("INSERT INTO serie (nome, descricao, baseado_em, classificacao, genero, elenco, duracao, idioma, ano_lancamento, num_temporada, num_episodios)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (
                       dados_serie['nome'],
                       dados_serie['descricao'],
                       dados_serie['baseado_em'],
                       dados_serie['classificacao'],
                       dados_serie['genero'],
                       dados_serie['elenco'],
                       dados_serie['duracao'],
                       dados_serie['idioma'],
                       dados_serie['ano_lancamento'],
                       dados_serie['num_temporada'],
                       dados_serie['num_episodios']
                   )
                   )


def retorna_series():
    cursor.execute("SELECT * FROM serie")
    return cursor.fetchall()


def retorna_serie(id):
    cursor.execute("SELECT * FROM serie WHERE id_serie = %s", [id])
    serie = cursor.fetchone()
    return serie


def atualiza_serie(serie):
    query = "UPDATE serie SET nome = %s, descricao = %s, baseado_em = %s, classificacao = %s, genero = %s, elenco = %s, duracao = %s, idioma = %s, ano_lancamento = %s, num_temporada = %s, num_episodios = %s" \
            "WHERE id_serie = %s"
    params = [serie['nome'], serie['descricao'], serie['baseado_em'], serie['classificacao'], serie['genero'], serie['elenco'], serie['duracao'], serie['idioma'], serie['ano_lancamento'], serie['num_temporada'], serie['num_episodios'], serie['id_serie']]

    cursor.execute(query, params)

def remove_serie(id):
    cursor.execute("DELETE FROM serie WHERE id_serie = %s", [id])