import tkinter as tk
from tkinter import font  as tkfont
from tkinter import ttk

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


class SampleApp(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry('800x270')

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
        button2 = tk.Button(self, text="Записи и поиск",
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
        button = tk.Button(self, text="Назад",
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
        frame1 = ScrollableFrame(self)

        label1 = tk.Label(self, text="Записи и поиск:", font=controller.title_font)
        label1.pack(side="top", fill="x", pady=10)
        label1.place(x=0, y=50)
        button1 = tk.Button(self, text="Назад",
                           command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="bottom")
        button1.place(x=40, y=200)



        frame1.pack(side="bottom", fill="x")
        frame1.place(x=180, y=50, width=600)
        entry = tk.Entry(self, width=55,)
        entry.pack()
        entry.place(x=180, y=10)
        def search(event):
            import sqlite3
            a = entry.get()

            conn = sqlite3.connect("DBforPhonebook")
            cursor = conn.cursor()
            for widget in frame1.scrollable_frame.winfo_children():
                widget.destroy()
            for row in cursor.execute('SELECT * FROM list WHERE Фамилия LIKE ?;', ('%'+a+'%',)):
                buf = tk.Label(frame1.scrollable_frame,
                               text=row,
                               font=controller.title_font)
                buf.pack()
        button2 = tk.Button(self, text="Поиск по фамилии/Вывод")
        button2.pack()
        button2.place(x=5, y=150)
        button2.bind('<Button-1>', search)

        label2 = tk.Label(self, text="Строка поиска:", font=controller.title_font)
        label2.pack()
        label2.place(x=0, y=10)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Редактор:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Назад",
                           command=lambda: controller.show_frame("StartPage"))
        button.place(x=10, y=400)
        button.pack(side="bottom")
        from tkinter import messagebox as mb

        def check(event):
            answer = mb.askyesno(title="Вопрос", message="Cохранить данные?")
            if answer == True:
                import sqlite3
                conn = sqlite3.connect("DBforPhonebook")
                cursor = conn.cursor()
                a = entry1.get()
                surname = e1.get()
                name = e2.get()
                patronymic = e3.get()
                phonenum = e4.get()
                comment = e5.get()

                cursor.execute('''UPDATE list SET Фамилия=?, Имя=?, Отчество=?,Номер=?, Комментарий=? WHERE ID=?;''',
                               (surname, name, patronymic, phonenum, comment, a,))
                conn.commit()





        label1 = tk.Label(self, text="*Фамилия:", font=controller.title_font)
        label1.pack(side="left", fill="x", pady=0, padx=0)
        label1.place(x=300, y=90)
        label2 = tk.Label(self, text="*Имя:", font=controller.title_font)
        label2.pack(side="left", fill="x", pady=0, padx=0)
        label2.place(x=300, y=120)
        label3 = tk.Label(self, text="*Отчество:", font=controller.title_font)
        label3.pack(side="left", fill="x", pady=0, padx=0)
        label3.place(x=300, y=150)
        label4 = tk.Label(self, text="*Номер телефона:", font=controller.title_font)
        label4.pack(side="left", fill="x", pady=0, padx=0)
        label4.place(x=300, y=180)
        label5 = tk.Label(self, text="Комментарий", font=controller.title_font)
        label5.pack(side="left", fill="x", pady=0, padx=0)
        label5.place(x=300, y=210)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)
        e4 = tk.Entry(self)
        e5 = tk.Entry(self)


        e1.pack(side="right")
        e1.place(x=500, y=90)
        e2.pack(side="right")
        e2.place(x=500, y=120)
        e3.pack(side="right")
        e3.place(x=500, y=150)
        e4.pack(side="right")
        e4.place(x=500, y=180)
        e5.pack(side="right")
        e5.place(x=500, y=210)



        button2 = tk.Button(self, text="Редактировать")
        button2.pack()
        button2.place(x=250, y=249)
        button2.bind('<Button-1>', check)

        entry1 = tk.Entry(self, width=3)
        entry1.pack()
        entry1.place(x=200, y=45)

        label1 = tk.Label(self, text="Введите ID изменяемого:")
        label1.pack()
        label1.place(x=10, y=50)

        label2 = tk.Label(self, text="Внесите изменения:")
        label2.pack()
        label2.place(x=400, y=50)





class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="This is page 4", font=controller.title_font)
        label1.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()





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