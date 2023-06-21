from data import questions
from question_model import Question
from game import Game

question_bank = []
for q in questions:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

new_game = Game(question_bank)

while new_game.still_continue():
    new_game.next_question()

print("You complete the quiz!")
print(f"Your score was {new_game.score}/{len(question_bank)}")
