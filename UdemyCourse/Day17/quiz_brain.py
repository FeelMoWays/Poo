class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    def check_answer(self,answer,acutal_answer):
        if answer.lower() == acutal_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You got it wrong")
        print(acutal_answer)
    def answer(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}:What would be the answer to this question: {current_question.text}: ")
        self.check_answer(answer=answer,acutal_answer=current_question.answer)