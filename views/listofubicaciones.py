import customtkinter
class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None,comandAddPath = None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.command = command
        self.comandAddPath = comandAddPath
        self.radiobutton_variable = customtkinter.StringVar()
        self.button_list = []
        self.label_list = []
        self.buttonVer_list = []
        self.labelNotfund = None

    def add_item(self,titleLabel, item,id_ubicaciones,tupla_cordenadas):

        button_agregar = customtkinter.CTkButton(self, text="agregar recorrido",font=('Bold',13), width=100, height=24)
        boton_ver = customtkinter.CTkButton(self, text='ver', width=100,font=('Bold',13), height=24) 
        label = customtkinter.CTkLabel(self,text=titleLabel,font=('Bold',17),text_color='white')
        if self.command is not None:
            boton_ver.configure(command=lambda: self.command(item,id_ubicaciones))
        if self.comandAddPath is not None:
             button_agregar.configure(command=lambda: self.comandAddPath(tupla_cordenadas,id_ubicaciones))
        button_agregar.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        boton_ver.grid(row=len(self.button_list), column=2, pady=(0, 10), padx=5)
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        self.button_list.append(button_agregar)
        self.buttonVer_list.append(boton_ver)
        self.label_list.append(label)
    def add_NotFound(self):
        self.labelNotfund = customtkinter.CTkLabel(self,text='Ubicaciones no encontradas',font=('Bold',22),text_color='red')
        self.labelNotfund.place(x=95,y=80)
    def remove_item(self):
        if self.labelNotfund != None:
             self.labelNotfund.destroy()
        for label, button,ver in zip(self.label_list, self.button_list,self.buttonVer_list):
                label.destroy()
                button.destroy()
                ver.destroy()
        self.label_list= []
        self.button_list=[]
        self.buttonVer_list=[]
               