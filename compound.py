# Соединение с базой данных mydatabase.db из папки instance и вывод всех записей

import sqlite3

comp = sqlite3.connect('instance/mydatabase_hw3.db')
cur = comp.cursor()
cur.execute('SELECT * FROM user')
print(cur.fetchall())
comp.close()
