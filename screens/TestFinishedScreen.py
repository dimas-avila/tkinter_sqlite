import tkinter as tk
from style import styles
from components.MainMenu import MainMenu

class TestFinishedScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.results = tk.StringVar(self)
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()
        
    def init_widgets(self):
        tk.Label(
            self,
            text="El examen ha finalizado! Estos son tus resultados: ",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
        
        tk.Label(
            self,
            textvariable=self.results,
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
        
        
        MainMenu(
            self,
            self.manager
        ).pack(
            **styles.PACK
        )