class Question:

    def __init__(self, question, correct_answer):
        self.category = "Geography"
        self.type = "boolean"
        self.difficulty = "easy"
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = not correct_answer
