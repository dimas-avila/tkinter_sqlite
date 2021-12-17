from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Models import Answer, Question, Test


if __name__ == "__main__":
    engine = create_engine(
        "sqlite:///C:\\Users\\lokix\\OneDrive\\Documents\\yotube\\src\\testsApp\\testsdb\\tests.db"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
      
    questions = [
        Question(
          question_text = "¿Cómo se define una lista?",
          answers = [
              Answer(
                  answer_text="lista=[1,2,3]",
                  is_correct=True
              ),
              Answer(
                  answer_text="lista=(1,2,3)",
                  is_correct=False
              ),
              Answer(
                  answer_text="iter(1,2,3)",
                  is_correct=False
              )
          ]
        ),
        
        Question(
            question_text="¿Qué excepción lanza un iterador?",
            answers=[
                Answer(
                    answer_text="StopIteration",
                    is_correct=True
                ),
                Answer(
                    answer_text="ZeroDivision",
                    is_correct=False
                ),
                Answer(
                    answer_text="SyntaxError",
                    is_correct=False
                )
            ]
        ),
        
        Question(
            question_text="¿Puedes modificar un elemento de una tupla?",
            answers=[
                Answer(
                    answer_text="Jamás",
                    is_correct=True
                ),
                Answer(
                    answer_text="Sí",
                    is_correct=False
                ),
            ]
        ),
    ]
    
    test = Test(test_name="Python", questions=questions)
    session.add(test)
    session.commit()
    