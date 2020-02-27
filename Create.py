def crte():
    import sqlite3
    conn = sqlite3.connect("DBforPhonebook")
    cursor = conn.cursor()
    surname = input("Введите фамилию:")
    name = input("Введите имя:")
    patronymic = input("Введите отчество:")
    phonenum = int(input("Введите номер телефона:"))
    comment = input("Введите комментарий(Не обязательно):")

    cursor.execute('''INSERT INTO list(Фамилия, Имя, Отчество, Номер, Комментарий) VALUES(?,?,?,?,?)''',
                   (surname, name, patronymic, phonenum, comment))

    conn.commit()

crte()

