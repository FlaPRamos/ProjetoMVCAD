# -- Arquivo Python que executa as funções CRUD(inserir, retornar, atualiza e apagar) do Episódio

from psycopg_connection import cursor

def insere_episodio(dados_episodio):

    cursor.execute("INSERT INTO episodio (nome, descricao, data_lancamento, id_serie, id_temporada)"
                   "VALUES (%s, %s, %s, %s, %s)",
                   (
                       dados_episodio['nome'],
                       dados_episodio['descricao'],
                       dados_episodio['data_lancamento'],
                       dados_episodio['id_serie'],
                       dados_episodio['id_temporada']
                   )
                   )


def retorna_episodios():
    cursor.execute("SELECT * FROM episodio")
    return cursor.fetchall()


def retorna_episodio(id):

    cursor.execute("SELECT * FROM episodio WHERE id_episodio = %s", [id])
    episodio = cursor.fetchone()
    return episodio


def atualiza_episodio(episodio):
    query = "UPDATE episodio SET nome = %s, descricao = %s, data_lancamento = %s,  id_serie = %s", "id_temporada = %s" \
            "WHERE id_episodio = %s"
    params = [episodio['nome'],  episodio['descricao'], episodio['data_lancamento'], episodio['id_serie'], episodio['id_temporada']]

    cursor.execute(query, params)

def remove_episodio(id):
    cursor.execute("DELETE FROM episodio WHERE id_episodio = %s", [id])