# -- CRUD Usuário

from psycopg_connection import cursor

def insere_usuario(dados_usuario):

    cursor.execute("INSERT INTO usuario (nome, data_nascimento, cpf, logradouro, numero, bairro,"
                   "cidade, uf, telefone, email, data_cadastro, ativo)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (
                       dados_usuario['nome'],
                       dados_usuario['data_nascimento'],
                       dados_usuario['cpf'],
                       dados_usuario['logradouro'],
                       dados_usuario['numero'],
                       dados_usuario['bairro'],
                       dados_usuario['cidade'],
                       dados_usuario['uf'],
                       dados_usuario['telefone'],
                       dados_usuario['email'],
                       dados_usuario['data_cadastro'],
                       dados_usuario['ativo']
                   )
                   )


def retorna_usuarios():
    cursor.execute("SELECT * FROM usuario")
    return cursor.fetchall()


def retorna_usuario(id):

    cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", [id])
    usuario = cursor.fetchone()
    return usuario


def atualiza_usuario(usuario):
    query = "UPDATE usuario SET nome = %s, data_nascimento = %s, cpf = %s, logradouro = %s, numero = %s, bairro = %s, cidade = %s, uf = %s, telefone = %s, email = %s, data_cadastro = %s, ativo = %s "\
            "WHERE id_usuario = %s"
    params = [usuario['nome'], usuario['data_nascimento'], usuario['cpf'], usuario['logradouro'], usuario['numero'], usuario['bairro'], usuario['cidade'], usuario['uf'], usuario['telefone'], usuario['email'], usuario['data_cadastro'], usuario['ativo'], usuario['id_usuario']]

    cursor.execute(query, params)

def remove_usuario(id):
    cursor.execute("DELETE FROM usuario WHERE id_usuario = %s", [id])