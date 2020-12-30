# Arquivo Python que gera relatório com todos as temporadas inteiras assistidas por um usuário

from psycopg_connection import cursor

def retorna_relatorio_temporada_x_usuario(id):
    cursor.execute("SELECT * FROM assiste_episodio, episodio, serie WHERE assiste_episodio.id_serie = episodio.id_serie and assiste_epsidio.id_usuario = %s", [id])
    temporada_x_usuario = cursor.fetchone()
    return temporada_x_usuario

if assiste_episodio.id_usuario = (id):
    num_episodio_assistido = 0
    for num_epsodio_assistido < temporada.num_episodios:
        if temporada.id_temporada = assiste_episodio.id_temporada
            num_epsodio_assistido = num_epsodio_assistido + 1

#exemplos
#query = '''
#SELECT  emp.first_name,
#        emp.last_name,
#       emp.gender,
#        depar.dept_name as departament_name,
#        dept.from_date,
#        dept.to_date
#FROM employees emp
#INNER JOIN dept_emp dept
#ON emp.emp_no = dept.emp_no
#INNER JOIN departments depar
#ON dept.dept_no = depar.dept_no;
#'''

#df = pd.read_sql_query(query,engine)
#df.head()



