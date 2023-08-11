import customtkinter

class List_opiniones_scrollable(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.textBox_list = []
        self.textbox_calificacion = []
        self.textbox_user = []
        self.textbox_destino = []

    def add_item(self,item,calificacion,name_user,name_destino,image=None):
        frame = customtkinter.CTkFrame(self,fg_color='white',width=700)
        textBox = customtkinter.CTkTextbox(frame,width=300,height=100,font=('Bold',12))
        textBox.pack(side=customtkinter.LEFT,padx=(3,3))
        textBox.insert("0.0","Comentario:\n\n"+item)

        text_box_calificacion = customtkinter.CTkTextbox(frame,width=100,height=100,font=('Bold',12))
        text_box_calificacion.pack(side=customtkinter.LEFT,padx=(3,3))
        text_box_calificacion.insert("0.0","Calificacion:\n\n"+calificacion)

        text_box_user = customtkinter.CTkTextbox(frame,width=140,height=100,font=('Bold',12))
        text_box_user.pack(side=customtkinter.LEFT,padx=(3,3))
        text_box_user.insert("0.0","Nombre de usuario:\n\n"+name_user)


        text_box_destino = customtkinter.CTkTextbox(frame,width=250,height=100,font=('Bold',12))
        text_box_destino.pack(side=customtkinter.LEFT,padx=(3,3))
        text_box_destino.insert("0.0","Nombre del restaurante:\n\n"+name_destino)
        
        frame.grid(row=len(self.textBox_list), column=0,pady=(0, 10), sticky="nsew")
        self.textBox_list.append(textBox)
        self.textbox_calificacion.append(text_box_calificacion)
        self.textbox_user.append(text_box_user)
    def remove_item(self, item):
        for textBox, text_box_calificacion,text_box_user, textbox_destino in zip(self.textBox_list,self.textbox_calificacion, self.textbox_user, self.textbox_destino):
            if item == textBox.cget("text"):
                textBox.destroy()
                text_box_calificacion.destroy()
                text_box_user.destroy()
                textbox_destino.destroy()
                self.textBox_list.remove(textBox)
                self.textbox_calificacion.remove(text_box_calificacion)
                self.textbox_user.remove(text_box_user)
                self.textbox_destino.remove(textbox_destino)
                return