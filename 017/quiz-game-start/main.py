from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


def game_init():
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


def game_run():
    quiz_brain = QuizBrain(question_bank)

    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    print(f"You've completed the quiz\nYour final score was {quiz_brain.score}/{quiz_brain.question_number}")


if __name__ == '__main__':
    game_init()
    game_run()