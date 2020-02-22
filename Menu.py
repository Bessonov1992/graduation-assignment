from tkinter import *
class main:
  def __init__(self, master):
    self.master = master
    self.master.title('Program')
    self.master.geometry('150x150+300+225')
    self.button = Button(self.master,
                         text = 'Создать запись',
                         command = self.openDialog)
    self.button.pack(side = TOP)
    self.button = Button(self.master,
                         text='Найти запись',
                         command=self.openDialog)
    self.button.pack(side=TOP)
    self.button = Button(self.master,
                         text='Редактировать запись',
                         command=self.openDialog)
    self.button.pack(side=TOP)
    self.button = Button(self.master,
                         text='Удалить запись',
                         command=self.openDialog)
    self.button.pack(side=TOP)
    self.button = Button(self.master,
                         text='Выйти из программы',
                         command=self.openDialog)
    self.button.pack(side=TOP)
    self.master.mainloop()

  def openDialog(self):
    child(self.master)
root = Tk()
main(root)

root.mainloop()