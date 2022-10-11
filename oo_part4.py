"""Solutions to part 4."""

from practice_part2 import Exam, Student, Question


class Quiz(Exam):
    """Quizzes for students.

    A quiz is like an exam, except that it is pass/fail.
    A quiz passes if more than 50% of answers are correct.
    """

    def administer(self):
        """Administer a quiz."""

        score = super(Quiz, self).administer()

        if score >= 0.5:
            return 1
        else:
            return 0


class StudentQuiz:
    """A quiz belonging to a particular student. Contains score for quiz."""

    def __init__(self, student, quiz):

        self.quiz = quiz
        self.student = student
        self.score = None

    def take_test(self):
        """Administer quiz to student and record score."""

        self.score = self.quiz.administer()

        if self.score:
            print("You passed!")

        else:
            print("Oh no! You failed!")


def example():
    """Show usage of quiz, questions, and student."""

    quiz = Quiz("Monday Quiz")

    parent_q = Question(
        "What is another term for a parent class?", "superclass"
    )
    quiz.add_question(parent_q)

    opinionated_q = Question(
        "What is the greatest programming language ever?", "Python"
    )
    quiz.add_question(opinionated_q)

    student = Student("Balloonicorn", "Jones", "777 Rainbow Road")

    balloonicorn_quiz = StudentQuiz(student, quiz)

    balloonicorn_quiz.take_test()
