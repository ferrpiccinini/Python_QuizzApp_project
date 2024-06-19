
class QuizBrainn:
    def __init__(self,correct_answer):
        self.correct_answerr = correct_answer

    def answer_checker(self,button_key_tf):
        if button_key_tf == self.correct_answerr:
            return True

