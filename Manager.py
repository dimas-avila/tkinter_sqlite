import tkinter as tk
from Controller import Controller
from screens.DeleteTestScreen import DeleteTestScreen
from screens.HomeScreen import HomeScreen
from screens.AddTestScreen import AddTestScreen
from screens.SelectTestScreen import SelectTestScreen
from screens.UpdateTestScreen import UpdateTestScreen
from screens.ExecuteTestScreen import ExecuteTestScreen
from screens.TestFinishedScreen import TestFinishedScreen

from style import styles

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Exámenes de Programación")
        self.controller = Controller()
        self.selected_test = ""
        self.num_questions = 0
        self.num_aciertos = 0
        self.questions = ""
        container = tk.Frame(self)
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(
            background=styles.BACKGROUND
        )
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        self.frames = {}
        
        pantallas = (HomeScreen, AddTestScreen, UpdateTestScreen, SelectTestScreen, ExecuteTestScreen, TestFinishedScreen, DeleteTestScreen)
        for F in pantallas:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
            
        self.show_frame(HomeScreen)
        
    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        
        
    # AQUÍ EMPIEZAN LAS TRANSICIONES DE PANTALLAS
    
    def home_to_create(self):
        self.show_frame(AddTestScreen)
        
    def home_to_update(self):
        new_options = self.get_test_names()
        self.frames[UpdateTestScreen].options.update_options(new_options)
        self.show_frame(UpdateTestScreen)
        
    def home_to_select(self):
        new_options = self.get_test_names()
        self.frames[SelectTestScreen].options.update_options(new_options)
        self.show_frame(SelectTestScreen)
        
    def home_to_delete(self):
        new_options = self.get_test_names()
        self.frames[DeleteTestScreen].options.update_options(new_options)
        self.show_frame(DeleteTestScreen)
        
    def select_to_execute(self):
        self.selected_test = self.frames[SelectTestScreen].options.selected.get()
        self.get_test()
        self.show_frame(ExecuteTestScreen)
        
    def execute_to_finish(self):
        self.frames[TestFinishedScreen].results.set(
            f"{self.num_aciertos} / {self.num_questions}"
        )
        self.num_aciertos = 0
        self.num_questions = 0
        self.show_frame(TestFinishedScreen)
    
    # AQUÍ EMPIEZAN LOS MÉTODOS DE LA BBDD

    def get_test_names(self):
        return self.controller.get_test_names()      
    
    def add_question(self, test_name, question_text, question_choices, correct_choice):
        self.controller.add_question(test_name, question_text, question_choices, correct_choice)
        
    def get_test(self):
        if self.selected_test != "":
            _questions = self.controller.get_test_questions(self.selected_test)
            self.questions = iter(_questions)
            self.frames[ExecuteTestScreen].init_widgets(next(self.questions))
            
    def delete_test(self, test_name):
        self.controller.delete_test(test_name)