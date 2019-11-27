from tkinter import  *
import Backend

class Front(object):
    def __init__(self, window):
        self.window = window
        self.window.title("This is a fance database project")
        self.myfont = ("Times New Roman", 18)
        self.yourfont = ("Times New Roman", 14)
        # need to create a backend instance here
        self.bk = Backend.Back()

        # let's create the widgets
        self.lb1 = Label(master=self.window, text="Title", font=self.myfont)
        self.lb1.grid(row=0, column=0, sticky="w", pady=5)

        self.lb2 = Label(master=self.window, text=" Year", font=self.myfont)
        self.lb2.grid(row=0, column=2, sticky="w", pady=5)

        self.lb3 = Label(master=self.window, text="Director", font=self.myfont)
        self.lb3.grid(row=1, column=0, sticky="w", pady=5)

        self.lb4 = Label(master=self.window, text=" Actress/Actor", font=self.myfont)
        self.lb4.grid(row=1, column=2, sticky="w", pady=5)

        # entrytext
        self.text_title = StringVar()
        self.et1 = Entry(master=self.window, textvariable=self.text_title, font=self.myfont)
        self.et1.grid(row=0, column=1)

        self.text_year = StringVar()
        self.et2 = Entry(master=self.window, textvariable=self.text_year, font=self.myfont)
        self.et2.grid(row=0, column=3)

        self.text_dir = StringVar()
        self.et3 = Entry(master=self.window, textvariable=self.text_dir, font=self.myfont)
        self.et3.grid(row=1, column=1)

        self.text_lead = StringVar()
        self.et4 = Entry(master=self.window, textvariable=self.text_lead, font=self.myfont)
        self.et4.grid(row=1, column=3)

        # main screen
        self.listbox =  Listbox(master=self.window, font=self.yourfont, height=10, width=80)
        self.listbox.grid(row=2, column=0, rowspan=8, columnspan=2, padx=20, pady=40)
        # need to bind an action for clicking in the listbox
        self.listbox.bind("ListboxSelect>>", func=self.get_row)

        self.scroll = Scrollbar(master=self.window)
        self.scroll.grid(row=2, column=2, rowspan=8, sticky="nsw", pady=40)
        # link it to the listbox
        self.scroll.configure(command=self.listbox.yview) # yviewscroll?

        # the buttons
        self.bt1 = Button(master=self.window, text="View all", font=self.myfont, command=self.view)
        self.bt1.grid(row=2, column=3)

        self.bt1 = Button(master=self.window, width=10, text="Delete", font=self.myfont, command=self.delete)
        self.bt1.grid(row=3, column=3)

        self.bt2 = Button(master=self.window, width=10, text="Add", font=self.myfont, command=self.add)
        self.bt2.grid(row=4, column=3)

        self.bt3 = Button(master=self.window, width=10, text="Search", font=self.myfont, command=self.view)
        self.bt3.grid(row=5, column=3)

        self.bt4 = Button(master=self.window, width=10, text="Update", font=self.myfont, command=self.view)
        self.bt4.grid(row=6, column=3)

        self.bt5 = Button(master=self.window, width=10, text="Close", font=self.myfont, command=self.view)
        self.bt5.grid(row=7, column=3)





    def get_row(self, action=None):
        # curselection returns a list of all the selected lines
        if not self.listbox.curselection():
            return
        line_num = self.listbox.curselection()[0]
        idx = self.listbox.get(line_num)[0]
        title = self.listbox.get(line_num)[1]
        year = self.listbox.get(line_num)[2]
        director = self.listbox.get(line_num)[3]
        lead = self.listbox.get(line_num)[4]
        self.text_title.set(title)
        self.text_year.set(year)
        self.text_dir.set(director)
        self.text_lead.set(lead)
        self.kept_index = self.listbox.get(line_num)[0]


    def view(self):
        data = self.bk.view_all()
        self.listbox.delete(0, END)
        for line in data:
            self.listbox.insert(END, line)

    def add(self):
        title = self.text_title.get()
        year = self.text_year.get()
        director = self.text_dir.get()
        lead = self.text_lead.get()
        self.bk.add_element(title, year, director, lead)
        self.view()

    def delete(self):
        # curselection returns a list of all the selected lines
        line_num = self.listbox.curselection()
        idx = self.listbox.get(line_num)[0]
        title = self.text_title.get()
        year = self.text_year.get()
        director = self.text_dir.get()
        lead = self.text_lead.get()
        self.bk.del_element(idx)
        self.view()

    def update(self):
        if not self.listbox.curselection():
            return
        line_num = self.listbox.curselection()[0]
        idx = self.listbox.get(line_num)[0]
        title = self.text_title.get()
        year = self.text_year.get()
        director = self.text_dir.get()
        lead = self.text_lead.get()
        self.bk.update_element((idx, title, year, director, lead))
        self.view()


    def close(self):
        exit(1)

window = Tk()
Front(window)
window.mainloop()
