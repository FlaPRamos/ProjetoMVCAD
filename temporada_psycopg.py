# -- CRUD Temporada

from psycopg_connection import cursor

def insere_temporada(dados_temporada):

    cursor.execute("INSERT INTO temporada (nome, descricao, data_lancamento, id_serie, num_episodios)"
                   "VALUES (%s, %s, %s, %s)",
                   (
                       dados_temporada['nome'],
                       dados_temporada['descricao'],
                       dados_temporada['data_lancamento'],
                       dados_temporada['id_serie'],
                       dados_temporada['num_episodios']
                   )
                   )


def retorna_temporadas():
    cursor.execute("SELECT * FROM temporada")
    return cursor.fetchall()


def retorna_temporada(id):

    cursor.execute("SELECT * FROM temporada WHERE id_temporada = %s", [id])
    temporada = cursor.fetchone()
    return temporada


def atualiza_temporada(temporada):
    query = "UPDATE temporada SET nome = %s, descricao = %s, data_lancamento = %s,  id_serie = %s, num_episodios = %s"\
            "WHERE id_temporada = %s"
    params = [temporada['nome'],  temporada['descricao'], temporada['data_lancamento'], temporada['id_serie'], temporada['num_episodios']]

    cursor.execute(query, params)

def remove_temporada(id):
    cursor.execute("DELETE FROM temporada WHERE id_temporada = %s", [id])