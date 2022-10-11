"""Solutions to part 1."""


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


class Exam:
    """An exam is a test.

    Exams comprise zero or more questions.
    """

    def __init__(self, name):
        self.name = name
        self.questions = []
