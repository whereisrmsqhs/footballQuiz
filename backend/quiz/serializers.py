from rest_framework import serializers
from .models import quizCategory


class QuizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = quizCategory
        fields = '__all__'
