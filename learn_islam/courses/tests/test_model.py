from django.test import TestCase

from ..models import Course


class CourseModelTests(TestCase):
    def setUp(self):
        Course.objects.create(level=1, order=1, slug="course-slug")

    def test_quiz_difficulties_with_no_quiz(self):
        c = Course.objects.get(slug="course-slug")

        self.assertEqual(c.quiz_difficulties, [])

    def test_quiz_difficulties_with_one_quiz(self):
        c = Course.objects.get(slug="course-slug")
        c.quiz_set.create(difficulty=1)

        self.assertEqual(c.quiz_difficulties, [1])

    def test_quiz_difficulties_with_two_quiz(self):
        c = Course.objects.get(slug="course-slug")
        c.quiz_set.create(difficulty=1)
        c.quiz_set.create(difficulty=1)

        self.assertEqual(c.quiz_difficulties, [1])

    def test_quiz_difficulties_with_two_quiz_two_difficulties(self):
        c = Course.objects.get(slug="course-slug")
        c.quiz_set.create(difficulty=1)
        c.quiz_set.create(difficulty=2)

        self.assertEqual(c.quiz_difficulties, [1, 2])

    def test_quiz_difficulties_with_three_quiz_two_difficulties(self):
        c = Course.objects.get(slug="course-slug")
        c.quiz_set.create(difficulty=1)
        c.quiz_set.create(difficulty=3)
        c.quiz_set.create(difficulty=3)

        self.assertEqual(c.quiz_difficulties, [1, 3])
