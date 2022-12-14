"""Solutions to part 2"""


class Student:
    """A student."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question:
    """A question in an exam."""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Pose a question.

        Shows the user the question, receives their answer,
        and returns True/False for if their answer is correct.
        """

        answer = input(self.question + " > ")
        return self.correct_answer == answer


class Exam:
    """An exam is a test."""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        """Add question to exam."""

        self.questions.append(question)

    def administer(self):
        """Administer a test, returning the score."""

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return 100 * (float(score) / len(self.questions))
