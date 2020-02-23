import sqlite3

conn = sqlite3.connect("BDforTB")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS bdfortb(ID integer PRIMARY KEY,
Фамилия text NOT NULL,
Имя text NOT NULL,
Отчество text NOT NULL,
Номер телефона integer NOT NULL,
Комментарий text NOT NULL)''')