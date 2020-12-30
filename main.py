# Arquivo Pytohn que importa a biblioteca CSV e chama as funções CRUD

import csv

from usuario_psycopg import insere_usuario, retorna_usuarios, retorna_usuario, atualiza_usuario, remove_usuario

 from filme_psycopg import insere_filme, retorna_filmes, retorna_filme, atualiza_filme, remove_filme

 from serie_psycopg import insere_serie, retorna_series, retorna_serie, atualiza_serie, remove_serie

def ler_arquivo():
    with open('mariaflix', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimiter=',')

        for usuario in leitor:
            cpf = usuario['cpf'].replace('.', '')
            usuario['cpf'] = cpf.replace('-', '')
            insere_usuario(usuario)

         for filme in leitor:
            insere_filme(filme)

        for serie in leitor:
           insere_serie(serie)


ler_arquivo()
