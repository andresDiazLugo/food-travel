import customtkinter as ctk
from views.listOpiniones import List_opiniones_scrollable
class Reviews(ctk.CTkFrame):
    def __init__(self,app,main) -> None:
        super().__init__(app,width=820,fg_color='orange',height=800)
        self.main = main
        self.render_element()
    def render_element(self):
        self.component_list_reviews = List_opiniones_scrollable(self,width=800,height=400,fg_color='#495057')
        self.component_list_reviews.place(x=0,y=100)
        self.list_calificaciones = self.main.calificacion_controller.return_all_reviews()
        if self.list_calificaciones is not False and len(self.list_calificaciones) > 0:
            for opiniones in self.list_calificaciones:
                name_user = self.main.calificacion_controller.return_name_user(opiniones['id_usuario'])
                name_destino = self.main.calificacion_controller.return_name_destino(opiniones['id_destino'])
                anonimo = name_user if  not opiniones['anonimo'] else 'anonimo'
                # print('ver las opiniones', opiniones['comentario'])
                self.component_list_reviews.add_item(opiniones['comentario'],opiniones['calificacion'],anonimo,name_destino)
        else:
            print('entrandooo')
            self.component_list_reviews.destroy()
            self.component_list_reviews.place_forget()
            self.description_label = ctk.CTkLabel(self,text='Tu historial esta vacio', text_color="white",font=ctk.CTkFont(family='Arial',size=40, weight="bold"))
            self.description_label.place(x=205,y=80)