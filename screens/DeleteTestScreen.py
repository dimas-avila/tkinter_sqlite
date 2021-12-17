import tkinter as tk
import tkinter.messagebox
from style import styles
from components.MainMenu import MainMenu
from components.SelectOption import SelectOption


class DeleteTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.option_list = self.manager.get_test_names()
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text="Selecciona el test que quieres eliminar",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        self.options = SelectOption(
            self,
            self.manager,
            self.option_list
        )

        self.options.pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="Eliminar",
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT,
            **styles.STYLE,
            command=lambda: self.delete_test()    
        ).pack(
            **styles.PACK
        )
        
        MainMenu(
            self,
            self.manager
        ).pack(
            **styles.PACK
        )

    def delete_test(self):
        _test_name = self.options.selected.get()
        tk.messagebox.showinfo(
            title="WARNING",
            message=f"¿Seguro que quieres eliminar {_test_name}?"
        )
        
        self.manager.delete_test(self.options.selected.get())
        
        tk.messagebox.showinfo(
            title="SUCCESS",
            message=f"El test {_test_name} ha sido eliminado?"
        )
        test_names = self.manager.get_test_names()
        self.options.update_options(test_names)

