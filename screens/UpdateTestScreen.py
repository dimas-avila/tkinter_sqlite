import tkinter as tk
from style import styles
from components.MainMenu import MainMenu
from components.SelectOption import SelectOption


class UpdateTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.option_list = self.manager.get_test_names()
        self.question_text = tk.StringVar(self)
        self.question_choices = tk.StringVar(self)
        self.correct_choice = tk.IntVar(self, 0)
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text="Selecciona el test a modificar",
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

        tk.Label(
            self,
            text="Enunciado de la pregunta: ",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        tk.Entry(
            self,
            textvariable=self.question_text,
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        tk.Label(
            self,
            text="Escribe las respuestas separadas por ';' : ",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        tk.Entry(
            self,
            textvariable=self.question_choices,
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        tk.Label(
            self,
            text="Número de la respuesta correcta (empieza en 0): ",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        final_input = tk.Entry(
            self,
            textvariable=self.correct_choice,
            justify=tk.CENTER,
            **styles.STYLE
        )

        final_input.pack(
            **styles.PACK
        )

        final_input.bind("<Return>", self.add_question)

        MainMenu(
            self,
            self.manager
        ).pack(
            **styles.PACK
        )

    def add_question(self, evenet):
        _question_text = self.question_text.get()
        _question_choices = self.question_choices.get().split(";")
        _correct_choice = self.correct_choice.get()
        _test_name = self.options.selected.get()

        info = f"Pregunta: {_question_text}\nRespuestas: {_question_choices}\nCorrecta: {_correct_choice}"
        
        self.manager.add_question(_test_name, _question_text, _question_choices, _correct_choice)

        self.question_text.set("")
        self.question_choices.set("")
        self.correct_choice.set("")
