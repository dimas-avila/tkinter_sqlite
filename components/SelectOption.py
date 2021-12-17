import tkinter as tk
from style import styles


class SelectOption(tk.Frame):
    
    def __init__(self, parent, manager, option_list):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.option_list = option_list
        self.selected = tk.StringVar(self)
        self.init_widgets()
        
    
    def init_widgets(self):
        self.options = tk.OptionMenu(
            self,
            self.selected,
            *self.option_list
        )
        
        self.options.config(**styles.STYLE)
        self.options["menu"].config(**styles.STYLE)
        self.options.pack(
            **styles.PACK
        )
    
    
    def update_options(self, new_options):
        menu = self.options["menu"]
        menu.delete(0, "end")
        
        for option in new_options:
            menu.add_command(
                label=option,
                command=lambda value=option: self.selected.set(value)
            )