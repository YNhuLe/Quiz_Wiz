class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 1
        self.question_list = question_list
        self.score = 0

    def still_have_question(self):
        """
        compare question number and length of question_list to check if there is still question
        :return:
        """
        return self.question_number < len(self.question_list)

    correct_input_format = True

    def check_input(self, cu_question):
        """
        check the input from user, if it is the format is right. If not give warning
        :param cu_question:
        :return:
        """
        while True:
            user_answer = input(f"Q.{self.question_number}: {cu_question.text} (True/False): ")

            if user_answer.lower() in ["true", "false"]:
                return user_answer
            else:
                print("Please give the correct answer either 'true' or 'false'")

    def next_question(self):
        """
        check answer from user if it is the right answer or not. Continue until the quiz complete.
        :return:
        """
        if self.still_have_question():
            current_question = self.question_list[self.question_number]
            user_answer = self.check_input(current_question)
            self.check_answer(user_answer, current_question.answer)
            self.question_number += 1
        else:
            print("No more question. Quiz completed!")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are correct!")
        else:
            print("You are incorrect!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def check_prize(self, score, question_list):
        """
        calculate the average, and define prize for player
        :param score:
        :param question_list:
        :return:
        """
        average = (score / len(question_list)) * 100
        if 35 <= average <= 50:
            print(f"Congrats!! You've won the Bronze Medal🥇😉 with {score}/{len(question_list)}")
        elif 50 < average <= 75:
            print(f"Congrats!! You've won the Silver Medal🥈😄 with {score}/{len(question_list)}")
        elif 75 < average <= 100:
            print(f"Well done!! You've won the Gold Cup🏆 🎊 with {score}/{len(question_list)}")
        else:
            print(f"You've got this, believe in yourself!!!🥉")
