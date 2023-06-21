class Game:
    def __init__(self, q_list):
        self.question_num = 0
        self.q_list = q_list
        self.score = 0

    def still_continue(self):
        return self.question_num < len(self.q_list)

    def next_question(self):
        current_q = self.q_list[self.question_num]
        self.question_num += 1
        user_answer = input(
            f"Q.{self.question_num} - {current_q.text} (True or False) :")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_a, correct_a):
        if user_a.lower() == correct_a.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_a}")
        print(f" Yor current socre is {self.score}/{self.question_num}")
