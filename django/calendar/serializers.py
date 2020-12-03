from rest_framework import serializers
from . import models


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True)
    year = serializers.StringRelatedField(many=False)
    month = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Question
        exclude = ('admin_published', 'admin_notes')


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Answer
        exclude = ('admin_approved', 'admin_notes')
