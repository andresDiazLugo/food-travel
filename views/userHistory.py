import customtkinter as ctk
from tkinter import messagebox
import os
from PIL import Image
from views.listHistoryUser import List_history_scrollable
class UserHistory(ctk.CTkFrame):
    def __init__(self,app,main):
        super().__init__(app,width=820,fg_color='orange',height=700)
        self.main = main
        self.render_elements()
    def render_elements(self):
        print('me ejecutooo')
        self.list_destinos = self.main.history_user_controller.return_all_history_path()
        # print('list_destinos',self.afterlist_destinos)
        if self.list_destinos is not False:
            self.component_list_history = List_history_scrollable(self,width=500,height=400,fg_color='#495057')
            self.component_list_history.place(x=140,y=100)
            self.button_delete_all = ctk.CTkButton(self,text="eliminar todo",fg_color='red',command=self.delete_all_history,font=('Bold',25))
            self.button_delete_all.place(x=310,y=540)
            for destino in self.list_destinos:
                current_directory = os.getcwd()
                file_path = os.path.join(current_directory,destino['imagen'])
                self.component_list_history.command = self.delete_id_user_history
                self.component_list_history.add_item(destino['id'],destino['nombre'],image=ctk.CTkImage(Image.open(file_path),size=(80, 80)))
        else:
            self.description_label = ctk.CTkLabel(self,text='Tu historial esta vacio', text_color="white",font=ctk.CTkFont(family='Arial',size=40, weight="bold"))
            self.description_label.place(x=205,y=80)
            self.component_list_history.destroy()
            self.button_delete_all.destroy()
            self.component_list_history.place_forget()  # Esto eliminará el espacio del componente eliminado
            self.button_delete_all.place_forget()  
    def delete_all_history(self):
        result = messagebox.askokcancel("Confirmación", "¿Estás seguro de eliminar todo tu historial?")
        if result:
            confirm_delete_history = self.main.history_user_controller.delete_all_history()
            if confirm_delete_history :
                self.render_elements()
                messagebox.showinfo("Éxito", "Tu historial fue borrado con exito.")
            else:
                print('surgio un error al eleminar todo tu historial')
    def delete_id_user_history(self,id):
        result = messagebox.askokcancel("Confirmación", "¿Estás seguro de eliminar este registro de tu historial?")
        if result:
            confirm_delete_history = self.main.history_user_controller.delete_user_history_id(id)
            if confirm_delete_history:
                 self.render_elements()
            else:
                print('surgio un error al eleminar un registro de tu historial')
            
        