from data import data_json
from quiz_brain import QuizBrainn
from ui import QuizInterface
import html

data = data_json["results"]
question_lists = []

for question in data_json["results"]:
    final_question = html.unescape(question["question"])
    question_lists.append((final_question, question["correct_answer"],))

QuizInterface(question_lists)


