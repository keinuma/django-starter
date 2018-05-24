from rest_framework import serializers

from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(
        many=True, source='choice_setZZ',
    )

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices')
