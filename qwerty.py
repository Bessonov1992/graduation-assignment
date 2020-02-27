import sqlite3

conn = sqlite3.connect("DBforPhonebook")
cursor = conn.cursor()

for row in cursor.execute('SELECT * FROM list'):
    print(row)