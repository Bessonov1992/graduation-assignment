import tkinter as tk
from tkinter import font  as tkfont


class SampleApp(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry('800x350')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Записная Книга", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Создать запись",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Записи",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Редактировать запись",
                            command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Удалить запись",
                            command=lambda: controller.show_frame("PageFour"))
        button5 = tk.Button(self, text="Выйти из программы",
                            command=lambda: controller.show_frame("PageFive"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="*Фамилия:", font=controller.title_font)
        label1.pack(side="left", fill="x", pady=0, padx=0)
        label1.place(x=30, y=30)
        label2 = tk.Label(self, text="*Имя:", font=controller.title_font)
        label2.pack(side="left", fill="x", pady=0, padx=0)
        label2.place(x=30, y=60)
        label3 = tk.Label(self, text="*Отчество:", font=controller.title_font)
        label3.pack(side="left", fill="x", pady=0, padx=0)
        label3.place(x=30,y=90)
        label4 = tk.Label(self, text="*Номер телефона:", font=controller.title_font)
        label4.pack(side="left", fill="x", pady=0, padx=0)
        label4.place(x=30, y=120)
        label5 = tk.Label(self, text="Комментарий", font=controller.title_font)
        label5.pack(side="left", fill="x", pady=0, padx=0)
        label5.place(x=30, y=150)
        label6 = tk.Label(self, text="Создать контакт", font=controller.title_font)
        label6.pack(side="top", fill="x", pady=0, padx=0)
        label6.place(x=150, y=0)
        button = tk.Button(self, text="Отмена",
                           command=lambda: controller.show_frame("StartPage"))
        def save(self):
            import sqlite3
            conn = sqlite3.connect("DBforPhonebook")
            cursor = conn.cursor()
            surname = e1.get()
            name = e2.get()
            patronymic = e3.get()
            phonenum = e4.get()
            comment = e5.get()

            cursor.execute('''INSERT INTO list(Фамилия, Имя, Отчество, Номер, Комментарий) VALUES(?,?,?,?,?)''',
                           (surname, name, patronymic, phonenum, comment))

            conn.commit()

        button2 = tk.Button(self, text="Сохранить")
        button2.bind('<Button-1>', save)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)
        e4 = tk.Entry(self)
        e5 = tk.Entry(self)

        button.pack(side="bottom")
        button.place(x=100, y=200)
        button2.pack(side="bottom")
        button2.place(x=200, y=200)
        e1.pack(side="right")
        e1.place(x=200, y=30)
        e2.pack(side="right")
        e2.place(x=200, y=60)
        e3.pack(side="right")
        e3.place(x=200, y=90)
        e4.pack(side="right")
        e4.place(x=200, y=120)
        e5.pack(side="right")
        e5.place(x=200, y=150)





class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def to_take(self):
            import sqlite3

            conn = sqlite3.connect("DBforPhonebook")
            cursor = conn.cursor()

            for row in cursor.execute('SELECT * FROM list'):
                print(row)

        label1 = tk.Label(self, text="Записи:", font=controller.title_font)
        label1.pack(side="top", fill="x", pady=10)
        label1.place(x=30, y=30)
        button1 = tk.Button(self, text="Назад",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Вывести")

        label2 = tk.Label(self, bg='gray', fg='yellow', width=50, height=15)
        label2.pack()
        label2.place(x=150, y=10)
        button1.pack(side="bottom")
        button1.place(x=40, y=200)
        button2.pack(side="bottom")
        button2.place(x=35, y=150)
        button2.bind('<Button-1>', to_take)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Уверенны,что хотите выйти?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Назад",
                           command=lambda: controller.show_frame("StartPage"))
        def quit(event):
            self.quit()

        button2 = tk.Button(self, text="Выход")
        button1.pack(side = "right")
        button1.place(x=0, y=0)
        button2.pack(side = "right")
        button2.place(x=1000, y=1000)
        button1.pack()
        button2.pack()
        button2.bind('<Button-1>', quit)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()