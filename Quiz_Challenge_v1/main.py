from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
is_continue = True
while is_continue:
    print("\n")
    keep_going = input("Welcome to the Quiz_Challenges game!! Please type 'yes' to play!😁 Or 'no' to exit the game: ")
    if keep_going.lower() == "yes":
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
            print("\nWe have rewards and rules for players:\n"
                  f"We have {len(question_bank)} questions\n"
                  "* If you've got from 35% - 50% question right out of the total number of questions. You will get "
                  "Bronze Medal🥇😉\n"
                  "* If you've got from 50% - 75% question right out of the total number of questions. You will get "
                  "the Silver Medal🥈😄\n"
                  "* If you've got from 75% - 100% question right out of the total number of questions. You will get "
                  "the Gold Cup🏆\n\n"
                  )
            quiz = QuizBrain(question_bank)
            while quiz.still_have_question():
                quiz.next_question()

            print("You've completed the quiz")
            quiz.check_prize(quiz.score, question_bank)
    elif keep_going.lower() == "no":
        print("So sad to see you go 🥺!!")
        is_continue = False
    else:
        print("Please type 'yes' to play!😁 Or 'no' to exit the game. ")


