import tkinter as tk
from style import styles
from components.MainMenu import MainMenu

class ExecuteTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        
        
    def init_widgets(self, question):
        self.manager.num_questions += 1
        self.helper_frame = tk.Frame(
            self
        )
        self.helper_frame.configure(background=styles.BACKGROUND)
        self.helper_frame.pack(**styles.PACK)
        
        self.question_text = tk.StringVar(self, question.question_text)
        self.selected_answer = tk.IntVar(self, question.answers[0].answer_id)
        
        tk.Label(
            self.helper_frame,
            textvariable=self.question_text,
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        id = -1
        for answer in question.answers:
            if answer.is_correct:
                id = answer.answer_id
            tk.Radiobutton(
                self.helper_frame,
                text=answer.answer_text,
                variable=self.selected_answer,
                value=answer.answer_id,
                activebackground=styles.BACKGROUND,
                activeforeground=styles.TEXT,
                **styles.STYLE
            ).pack(
                styles.PACK
            )
            
        tk.Button(
            self.helper_frame,
            text="Next Question",
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT,
            **styles.STYLE,
            command=lambda: self.next_question(id)
        ).pack(
                styles.PACK
        )
        
        MainMenu(
            self.helper_frame,
            self.manager
        ).pack(
            **styles.PACK
        )
        
    def check_answer(self, correct_id):
        if self.selected_answer.get() == correct_id:
            self.manager.num_aciertos +=1
            
    def next_question(self, correct_id):
        try:
            self.helper_frame.pack_forget()
            self.helper_frame.destroy()
            self.check_answer(correct_id)
            self.init_widgets(next(self.manager.questions))
        except StopIteration:
            print("No more questions")
            self.manager.execute_to_finish()