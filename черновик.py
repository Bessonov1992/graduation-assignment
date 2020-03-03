import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
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
        button2 = tk.Button(self, text="Найти запись",
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
        label = tk.Label(self, text="Создать контакт", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Отмена",
                           command=lambda: controller.show_frame("StartPage"))

        button2 = tk.Button(self, text="Сохранить",
                           command = self.insert_BULK_DATA())
        button.pack()
        button2.pack()

    def insert_BULK_DATA(self):
        import sqlite3
        conn = sqlite3.connect("DBforPhonebook")
        cursor = conn.cursor()
        surname = "Введите фамилию:"
        name = "Введите имя:"
        patronymic = "Введите отчество:"
        phonenum = 123
        comment = "Введите комментарий(Не обязательно):"

        cursor.execute('''INSERT INTO list(Фамилия, Имя, Отчество, Номер, Комментарий) VALUES(?,?,?,?,?)''',
                       (surname, name, patronymic, phonenum, comment))

        conn.commit()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


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
        label = tk.Label(self, text="This is page 5", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()