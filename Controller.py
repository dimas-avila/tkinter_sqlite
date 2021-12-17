from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from Models import Answer, Question, Test
from sqlite3 import ProgrammingError

class Controller:
    def __init__(self) -> None:
        engine = create_engine(
            "sqlite:///C:\\Users\\lokix\\OneDrive\\Documents\\yotube\\src\\testsApp\\testsdb\\tests.db"
        )
        Session = sessionmaker(bind=engine)
        self.session = Session()
        
    
    def create_empty_test(self, _test_name):
        test = self.session.query(Test).filter(Test.test_name == _test_name).first()
        if test == None:
            new_test = Test(test_name = _test_name)
            self.session.add(new_test)
            self.session.commit()
        else:
            raise ProgrammingError("Test already exists")
        
    
    def get_test_names(self):
        tests = self.session.query().with_entities(Test.test_name).all()
        test_names = [test[0] for test in tests]
        return test_names
    
    
    def add_question(self, test_name, question_text, question_choices, correct_choice):
        test = self.session.query(Test).filter(Test.test_name == test_name).first()
        
        _answers = [
            Answer(
                answer_text=choice,
                is_correct=correct_choice == idx,
            ) for idx, choice in enumerate(question_choices)
        ]
        
        question = Question(
            question_text=question_text,
            answers=_answers,
            test_id=test.test_id
        )
        
        self.session.add(question)
        self.session.commit()
            

    def get_test_questions(self, test_name):
        test = self.session.query(Test).filter(Test.test_name == test_name).first()
        return test.questions
    
    def delete_test(self, test_name):
        test = self.session.query(Test).filter(Test.test_name == test_name).first()
        self.session.delete(test)
        self.session.commit()
        
        
"""if __name__ == "__main__":
    c = Controller()
    c.get_test_names()"""
        
    