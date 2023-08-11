import customtkinter
class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None,comandAddPath = None,comandCalificacion=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.command = command
        self.comandAddPath = comandAddPath
        self.comandCalificacion = comandCalificacion
        self.radiobutton_variable = customtkinter.StringVar()
        self.frame = []
        self.button_list = []
        self.label_list = []
        self.buttonVer_list = []
        self.buttonCalificar = []
        self.labelNotfund = None

    def add_item(self,titleLabel, item,id_ubicaciones,tupla_cordenadas):
        frame = customtkinter.CTkFrame(self,fg_color='#252422')
        button_agregar = customtkinter.CTkButton(frame, text="agregar recorrido",font=('Bold',13), width=100, height=24)
        boton_ver = customtkinter.CTkButton(frame, text='ver', width=50,font=('Bold',13), height=24) 
        boton_calificacion = customtkinter.CTkButton(frame, text='calificar',width=50,font=('Bold',13)) 
        label = customtkinter.CTkLabel(frame,text=titleLabel,font=('Bold',17),text_color='white')
        if self.command is not None:
            boton_ver.configure(command=lambda: self.command(item,id_ubicaciones))
        if self.comandAddPath is not None:
            button_agregar.configure(command=lambda: self.comandAddPath(tupla_cordenadas,id_ubicaciones))
        if self.comandCalificacion is not None:
            boton_calificacion.configure(command=lambda: self.comandCalificacion(id_ubicaciones)) 
        label.pack(side=customtkinter.LEFT,pady=(15, 15))
        button_agregar.pack(side=customtkinter.RIGHT,pady=(10, 10),padx=(5,0))
        boton_ver.pack(side=customtkinter.RIGHT,pady=(10, 10),padx=(5,0))
        boton_calificacion.pack(side=customtkinter.RIGHT,pady=(10, 10),padx=(5,0))
        frame.grid(row=len(self.label_list), column=0,pady=(10, 10), sticky="nsew")
        self.button_list.append(button_agregar)
        self.buttonVer_list.append(boton_ver)
        self.buttonCalificar.append(boton_calificacion)
        self.label_list.append(label)
        self.frame.append(frame)
    def add_NotFound(self):
        frame = customtkinter.CTkFrame(self,fg_color='#252422')
        frame.grid(row=0, column=0,pady=(10, 10), sticky="nsew")
        self.labelNotfund = customtkinter.CTkLabel(frame,text='Ubicaciones no encontradas',font=('Bold',22),text_color='red')
        self.labelNotfund.pack()
    def remove_item(self):
        if self.labelNotfund != None:
             self.labelNotfund.destroy()
        for label, button,ver,calificar,frame in zip(self.label_list, self.button_list,self.buttonVer_list,self.buttonCalificar,self.frame):
                label.destroy()
                button.destroy()
                ver.destroy()
                calificar.destroy()
                frame.destroy()
                
        self.label_list= []
        self.button_list=[]
        self.buttonVer_list=[]
        self.buttonCalificar=[]
        self.frame=[]