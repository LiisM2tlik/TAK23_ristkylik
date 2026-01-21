
from tkinter import Tk
from tkinter import *


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__width = 600
        self.__height = 500

        self.title('Ristküliku arvutaja')
        self.center_window(self.__width, self.__height)

        self.top_frame = self.create_top_frame()  # siia peale tulevad kaks leibelit - pikkus laius, textboxid ja nupp - arvuta
        self.bottom_frame = self.create_bottom_frame()  # siia tuleb textbox tulemustega.

        self.btn_send, self.text_box, self.num_pikkus, self.num_laius, self.features = self.create_frame_features()

        self.bind('<Return>', self.controller.arvuta_click)

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame = Frame(self, bg='grey', height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='lightgrey')
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_features(self):
        lbl_info1 = Label(self.top_frame, text='Ristküliku pikkus')
        lbl_info1.grid(row=0, column=0, padx=5, pady=5)

        lbl_info2 = Label(self.top_frame, text='Ristküliku laius')
        lbl_info2.grid(row=1, column=0, padx=5, pady=5)

        num_pikkus = Entry(self.top_frame)
        num_pikkus.grid(row=0, column=1, padx=5, pady=5)
        num_pikkus.focus()

        num_laius = Entry(self.top_frame)
        num_laius.grid(row=1, column=1, padx=5, pady=5)

        btn_send = Button(self.top_frame, text='Arvuta', command=self.controller.arvuta_click)
        btn_send.grid(row=1, column=2, padx=5, pady=5)

        text_box = Text(self.bottom_frame, state='disabled')
        text_box.pack(expand=True, fill=BOTH, padx=5, pady=5)

        return btn_send, text_box, num_pikkus, num_laius, lbl_info1

