from tkinter import *
from tkinter import ttk


class WinMain:
    def __init__(self, master):
        self.master = master
        # root win config
        self.master.title("DIY Winery Log")
        self.master.geometry("768x667+5+5")  # self.resizable(0, 0)
        # menu config
        self.master.menu_bar = Frame(self.master)
        self.display_menu()
        self.master.menu_bar.pack(side=TOP, expand=YES, fill=X)
        # main frame config

        # start loop
        self.master.mainloop()

    # OPEN MENU NEW PROJECT WINDOW
    def open_menu_new_project_win(self):
        pass
        # new_project_win = WorkingPlace(title='Create New Winemaking Project',
        #                                purpose='start')  # <start> new project, <record> a progress or <analize> results

    # OPEN MENU ABOUT WINDOW
    def open_menu_about_win(self):
        about_win = Toplevel(self.master)
        about_win.title("About the DIY Winery Log")
        about_win.geometry("320x200+10+10")
        Label(about_win,
              text="\nThis DIY Winery Log is a pet-project\n\nver.2022.1.0.En\n\ncoding: Vladimir Konovalov\n\nfor free distribution ❦\n\nFeedback: k4cooperation@outlook.com",
              font=("Helvetica", "12"), padx=10, pady=10).pack()

    # OPEN MENU HELP WINDOW
    def open_menu_help_win(self):
        help_win = Toplevel(self.master)
        help_win.title("FAQ")
        help_win.geometry('768x667+10+10')
        # lbl_H1 = Label(help_win, text="Frequently Asked Questions", font=("Helvetica", "16"), padx=10, pady=10)
        # lbl_H1.place(x=35, y=10)

    def display_menu(self):
        # MENU
        menu = Menu(self.master)  # menu bar added in init foo
        self.master.config(menu=menu)

        # ADD FILE ITEM
        menu_item_file = Menu(menu, tearoff=0)  # add <File> item in main menu <, tearoff=0> - cannot tear off menu
        menu_item_file.add_command(label='New winemaking project', command=self.open_menu_new_project_win)
        menu_item_file.add_command(label='Open project')
        menu_item_file.add_separator()  # add item in menu item <File>
        menu_item_file.add_command(label='Exit', command=self.master.destroy)

        # ADD REPORTS ITEM
        menu_item_reports = Menu(menu,
                                 tearoff=0)  # add <Reports> item in main menu <, tearoff=0> - cannot tear off menu
        menu_item_reports.add_command(label='Find project')  # add item in menu item <Reports>
        menu_item_reports.add_command(label='In production')
        menu_item_reports.add_command(label='Log archive')

        # ADD HELP ITEM
        menu_item_help = Menu(menu, tearoff=0)  # add <Help> item in main menu <, tearoff=0> - cannot tear off menu
        menu_item_help.add_command(label='Help', command=self.open_menu_help_win)  # add item in menu item <Help>
        menu_item_help.add_separator()
        menu_item_help.add_command(label='About', command=self.open_menu_about_win)

        # LINK MENU ITEMS WITH
        menu.add_cascade(label="File", menu=menu_item_file)
        menu.add_cascade(label="Reports", menu=menu_item_reports)
        menu.add_cascade(label="Help", menu=menu_item_help)

