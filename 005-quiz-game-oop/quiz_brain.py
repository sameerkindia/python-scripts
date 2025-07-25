class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): ")
        print(user_input)
        self.check_answer(current_question.answer, user_input)


    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("That's wrong")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
