from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    first_text_answer = Question(question_text,question_answer)
    question_bank.append(first_text_answer)

printing=QuizBrain(question_bank)
while printing.still_have_question():
    printing.next_question()
