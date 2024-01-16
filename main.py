from question_model import Quesans
from data import question_data
from quiz_brain import QuizBrain
# create empty list and loop through the list items to take out text and answer which
question_list=[]
for item in question_data:
    question_text=item["text"]
    answer=item["answer"]
    #object created and positional arguement used 
    new_question=Quesans(question_text,answer)
    question_list.append(new_question)
#print(question_list)    

#create a quizbrain class object
quiz=QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")