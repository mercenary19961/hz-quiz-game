import random
from question_bank import question_bank as q_bank

class QuizBrain():
    def __init__(self):
        self.questions = q_bank
        self.asked_questions = []
        
    def easy_question_call(self):
        if len(self.asked_questions) >= 30:
             return None,None,None
        while True:
                q_num = random.randint(0,29)
                if q_num not in self.asked_questions:
                    q = self.questions[0]["questions"][q_num]["question"]
                    a_options = self.questions[0]["questions"][q_num]["options"]
                    a = self.questions[0]["questions"][q_num]["answer"]
                    self.asked_questions.append(q_num)
                    break
                    
        return q,a_options,a
    
    def medium_question_call(self):
        if len(self.asked_questions) >= 30:
             return None,None,None
        while True:
                q_num = random.randint(0,29)
                if q_num not in self.asked_questions:
                    q = self.questions[1]["questions"][q_num]["question"]
                    a_options = self.questions[1]["questions"][q_num]["options"]
                    a = self.questions[1]["questions"][q_num]["answer"]
                    self.asked_questions.append(q_num)
                    break
                    
        return q,a_options,a
    
    def hard_question_call(self):
        if len(self.asked_questions) >= 30:
             return None,None,None
        while True:
                q_num = random.randint(0,29)
                if q_num not in self.asked_questions:
                    q = self.questions[2]["questions"][q_num]["question"]
                    a_options = self.questions[2]["questions"][q_num]["options"]
                    a = self.questions[2]["questions"][q_num]["answer"]
                    self.asked_questions.append(q_num)
                    break
                    
        return q,a_options,a