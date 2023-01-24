from functools import partial
from tkinter import *
from data import DataProcessing
from network import PcControl
from tkinter import messagebox
import os

# Constants
C_WINDOW_WIDTH = 1000
C_WINDOW_HEIGHT = 600


class MainScene(DataProcessing, PcControl):
    pos_y = 10  # Position of widgets on the y-axis
    count_id = 0  # Count the number of buttons initialized

    def __init__(self):
        """Initializes the main scene."""

        super().__init__()
        self.root = Tk()
        self.root.title("PC")
        self.root.geometry(str(C_WINDOW_WIDTH) + "x" + str(C_WINDOW_HEIGHT))
        self.root.resizable(False, False)

        frame_title = Frame(self.root, relief=RAISED, borderwidth=1)  # Frame for title
        frame_title.pack(fill=BOTH)
        title = Label(frame_title, text='List of computers', font=('Microsoft Yahei UI Light', 25), pady=10)
        title.pack()

        Button(frame_title, width=10, bg="lightgray", text='Add new PC', font=('Microsoft Yahei UI Light', 12),
               border=1,
               relief=RAISED, command=self.open_child_scene).place(x=870, y=15)

        """Initializing labels with column names"""
        frame_data = Frame(self.root, relief=RAISED)  # Frame for data pc
        frame_data.pack(fill=BOTH)
        pc_numbers = Label(frame_data, text="№", font=('Microsoft Yahei UI Light', 12), width=4,
                           borderwidth=2, relief="solid", highlightcolor="black")
        pc_numbers.pack(side=LEFT, anchor=N, padx=5, pady=5)

        ip_title = Label(frame_data, text='IP-addr', font=('Microsoft Yahei UI Light', 12), width=12, borderwidth=2,
                         relief="solid",
                         highlightcolor="black")
        ip_title.pack(side=LEFT, anchor=N, padx=5, pady=5)

        mac_title = Label(frame_data, text='Mac-addr', font=('Microsoft Yahei UI Light', 12), width=16, borderwidth=2,
                          relief="solid",
                          highlightcolor="black")
        mac_title.pack(side=LEFT, anchor=N, padx=5, pady=5)

        port_title = Label(frame_data, text='Port', font=('Microsoft Yahei UI Light', 12), width=7, borderwidth=2,
                           relief="solid",
                           highlightcolor="black")
        port_title.pack(side=LEFT, anchor=N, padx=5, pady=5)

        user_title = Label(frame_data, text='Username', font=('Microsoft Yahei UI Light', 12), width=16,
                           borderwidth=2,
                           relief="solid",
                           highlightcolor="black")
        user_title.pack(side=LEFT, anchor=N, padx=5, pady=5)

        password_title = Label(frame_data, text='Password', font=('Microsoft Yahei UI Light', 12), width=10,
                               borderwidth=2,
                               relief="solid",
                               highlightcolor="black")
        password_title.pack(side=LEFT, anchor=N, padx=5, pady=5)

        switch_title = Label(frame_data, text='Switch', font=('Microsoft Yahei UI Light', 12), width=10,
                             borderwidth=2,
                             relief="solid",
                             highlightcolor="black")
        switch_title.pack(side=LEFT, anchor=N, padx=5, pady=5)

        status_title = Label(frame_data, text='Status', font=('Microsoft Yahei UI Light', 12), width=10, borderwidth=2,
                             relief="solid",
                             highlightcolor="black")
        status_title.pack(side=LEFT, anchor=N, padx=5, pady=5)

        delete_title = Label(frame_data, text='Delete', font=('Microsoft Yahei UI Light', 12), width=10, borderwidth=2,
                             relief="solid",
                             highlightcolor="black")
        delete_title.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.displaying_hosts()

    def displaying_hosts(self):
        """This function creates and outputs a list of computers"""

        frame = Frame(self.root, relief=RAISED, width=1000, height=298)
        frame.place(x=0, y=100)

        for _ in self.data_sheet:
            Frame(frame, width=1100, height=2, bg='black').place(x=0, y=self.pos_y - 4)

            number_pc = Label(frame, text=self.count_id + 1, fg="black",
                              font=('Microsoft Yahei UI Light', 9, 'bold'))
            number_pc.place(x=20, y=self.pos_y)

            # Computer data
            data = self.data_sheet[self.count_id].split(',')

            ip = Label(frame, text=data[2], fg="black",
                       font=('Microsoft Yahei UI Light', 9, 'bold'))
            ip.place(x=60, y=self.pos_y)

            mac = Label(frame, text=data[3], fg="black",
                        font=('Microsoft Yahei UI Light', 9, 'bold'))
            mac.place(x=180, y=self.pos_y)

            port = Label(frame, text=data[4], fg="black",
                         font=('Microsoft Yahei UI Light', 9, 'bold'))
            port.place(x=360, y=self.pos_y)

            user = Label(frame, text=data[0], fg="black",
                         font=('Microsoft Yahei UI Light', 9, 'bold'))
            user.place(x=440, y=self.pos_y)

            password = Label(frame, text=data[1], fg="black",
                             font=('Microsoft Yahei UI Light', 9, 'bold'))
            password.place(x=590, y=self.pos_y)

            Button(frame, width=4, bg="lightgray", text='OFF', border=1, relief=RAISED,
                   command=partial(self.off_pc, self.count_id)).place(x=730, y=self.pos_y)

            Button(frame, width=4, bg="lightgray", text='ON', border=1,
                   command=partial(self.on_pc, self.count_id)).place(
                x=690, y=self.pos_y)

            Button(frame, width=4, bg="lightgray", border=1, relief=RAISED,
                   command=partial(self.status_pc, self.count_id)).place(x=820, y=self.pos_y)

            Button(frame, width=4, text='X', bg="lightgray", border=1, relief=RAISED,
                   command=partial(self.__delete_pc__, self.count_id)).place(x=925, y=self.pos_y)

            self.pos_y += 30
            self.count_id += 1

        Frame(frame, width=1000, height=2, bg='black').place(x=0, y=self.pos_y - 4)

    def __delete_pc__(self, count_id):
        super().__delete_pc__(count_id)
        self.root.destroy()
        os.system("gui.py")

    def status_pc(self, count_id):
        if super().status_pc(count_id):
            messagebox.showinfo('Status', 'This computer is turned on')
        else:
            messagebox.showerror('Status', 'This computer is turned off')

    def off_pc(self, count_id):
        if super().off_pc(count_id):
            messagebox.showinfo('Switching power', 'This computer was shut down successfully')
        else:
            messagebox.showerror('Switching power', 'ERROR')

    def open_child_scene(self):
        AddPcScene(self.root)

    def run(self):
        self.root.mainloop()


class AddPcScene:
    def __init__(self, parent):
        """Initializes the child scene."""

        self.root = Toplevel(parent)
        self.root.title("Add new PC")
        self.root.geometry('925x500+300+200')
        self.root.configure(bg='#fff')
        self.root.resizable(False, False)

        """Initializing rows for data entry"""
        main_frame = Frame(self.root, width=900, height=450, bg='#fff')
        main_frame.place(x=12, y=12)

        self.username = Entry(main_frame, width=25, fg='black', border=0, bg='white',
                              font=('Microsoft Yahei UI Light', 11))
        self.username.place(x=305, y=100)
        self.username.insert(0, 'Username')
        Frame(main_frame, width=295, height=2, bg='black').place(x=300, y=127)

        self.password = Entry(main_frame, width=25, fg='black', border=0, bg='white',
                              font=('Microsoft Yahei UI Light', 11))
        self.password.place(x=305, y=150)
        self.password.insert(0, 'Password')
        Frame(main_frame, width=295, height=2, bg='black').place(x=300, y=177)

        self.ip_addr = Entry(main_frame, width=25, fg='black', border=0, bg='white',
                             font=('Microsoft Yahei UI Light', 11))
        self.ip_addr.place(x=305, y=200)
        self.ip_addr.insert(0, 'IP')
        Frame(main_frame, width=295, height=2, bg='black').place(x=300, y=227)

        self.mac_addr = Entry(main_frame, width=25, fg='black', border=0, bg='white',
                              font=('Microsoft Yahei UI Light', 11))
        self.mac_addr.place(x=305, y=250)
        self.mac_addr.insert(0, 'MAC-address')
        Frame(main_frame, width=295, height=2, bg='black').place(x=300, y=277)

        self.net_port = Entry(main_frame, width=25, fg='black', border=0, bg='white',
                              font=('Microsoft Yahei UI Light', 11))
        self.net_port.place(x=305, y=300)
        self.net_port.insert(0, 'Port')
        Frame(main_frame, width=295, height=2, bg='black').place(x=300, y=327)

        Button(main_frame, width=39, pady=7, text='Add', border=1,
               command=partial(self.add_new_pc, parent)).place(x=600, y=400)

        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def add_new_pc(self, parent):
        username = self.username.get()
        password = self.password.get()
        ip_addr = self.ip_addr.get()
        mac_addr = self.mac_addr.get()
        net_port = self.net_port.get()

        if DataProcessing().__add_pc__(username, password, ip_addr, mac_addr, net_port):
            messagebox.showinfo('Add', 'Computer successfully added')
            self.root.destroy()
            parent.destroy()
            os.system('gui.py')

        else:
            messagebox.showerror('Error', 'Incorrect mac or ip address entered')


def main():
    window = MainScene()
    window.run()


if __name__ == "__main__":
    main()
