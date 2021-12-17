import tkinter as tk
from style import styles
from components.MainMenu import MainMenu
from components.SelectOption import SelectOption


class SelectTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.option_list = self.manager.get_test_names()
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text="Selecciona el test que quieras realizar",
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
            text="Start Test",
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT,
            **styles.STYLE,
            command=lambda: self.manager.select_to_execute()    
        ).pack(
            **styles.PACK
        )
        
        MainMenu(
            self,
            self.manager
        ).pack(
            **styles.PACK
        )


