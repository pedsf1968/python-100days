# Get questions to API https://opentdb.com/api.php?amount=10

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzlerUI


question_bank = []


def init_question_datas():
    global question_bank
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


def main():
    init_question_datas()

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizzlerUI(quiz)
    # while quiz.still_has_questions():
    #     quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()