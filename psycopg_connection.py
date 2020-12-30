# -- PSYCOPG CONNECTION --

import psycopg2


conn = psycopg2.connect("dbname=mariaflix user=postgres password=passbd2020 host=localhost")

conn.autocommit = True

cursor = conn.cursor()