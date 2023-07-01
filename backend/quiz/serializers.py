from rest_framework import serializers
from .models import quizCategory, imageQuizQnA


class ImageQuizQnASerializer(serializers.ModelSerializer):

    question = serializers.ImageField(use_url=True, required=False)
    # created = serializers.TimeField(required=False)
    # answer = serializers.CharField(required=False)
    # quizCategory = serializers.CharField(required=False)
    class Meta:
        model = imageQuizQnA
        fields = ('quiz_category', 'created', 'question', 'answer')

class QuizCategorySerializer(serializers.ModelSerializer):
    imagequizqna = ImageQuizQnASerializer(many=True, read_only=True)
    class Meta:
        model = quizCategory
        fields = ('created', 'title','intro','rule', 'imagequizqna')