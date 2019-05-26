import pytest
import django.utils.timezone
from learn_islam.quizzes import models

pytestmark = pytest.mark.django_db

def test_quizzes_models_creation():
    before = django.utils.timezone.now()
    models.Quiz.objects.create(
        difficulty=1
    )

    quizzes = models.Quiz.objects.all()
    assert quizzes.count() == 1
    assert quizzes[0].difficulty == 1
    assert quizzes[0].pub_date >= before
    assert quizzes[0].pub_date <= django.utils.timezone.now()
