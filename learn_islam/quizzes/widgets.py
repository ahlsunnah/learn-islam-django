from django import forms

class Quiz(forms.Widget):
    class Media:
        js = [
            # TODO: include 'https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js', in development
            'https://cdn.jsdelivr.net/npm/vue@2.6.10',
            'quizzes/js/quiz.js'
        ]

    template_name = 'quizzes/widgets/quiz.html'
