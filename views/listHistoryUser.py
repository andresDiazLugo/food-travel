import customtkinter
import os
from PIL import Image

class List_history_scrollable(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self,id, item, image=None):
        frame = customtkinter.CTkFrame(self,fg_color='white',width=700)
        label = customtkinter.CTkLabel(frame, text=item,image=image, compound="left", padx=0, anchor="w",font=('Bold',20))
        button = customtkinter.CTkButton(frame, text="eliminar",fg_color='red', width=100, height=24,font=('Bold',15))
        if self.command is not None:
            button.configure(command=lambda: self.command(id))
        label.pack(side=customtkinter.LEFT)
        button.pack(side=customtkinter.RIGHT)
        frame.grid(row=len(self.label_list), column=0,pady=(0, 10), sticky="nsew")
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return