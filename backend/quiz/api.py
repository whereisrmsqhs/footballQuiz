from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class QuizCategoryList(APIView):
    def get(self, request):
        model = quizCategory.objects.all()
        serializer = QuizCategorySerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuizCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizCategoryDetail(APIView):
    def get(self, request, title):
        model = quizCategory.objects.get(title=title)
        serializer = QuizCategorySerializer(model)
        return Response(serializer.data)

    def put(self, request, title):
        model = quizCategory.objects.get(title=title)
        serializer = QuizCategorySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, title):
        model = quizCategory.objects.get(title=title)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class imageQuizQnAList(APIView):
    def get(self, request):
        model = imageQuizQnA.objects.all()
        serializer = ImageQuizQnASerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageQuizQnASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class imageQuizQnADetail(APIView):
    def get(self, request, id):
        model = imageQuizQnA.objects.get(id=id)
        serializer = ImageQuizQnASerializer(model)
        return Response(serializer.data)

    def delete(self, request, id):
        model = imageQuizQnA.objects.get(id=id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)