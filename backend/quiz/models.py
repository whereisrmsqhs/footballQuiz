from django.db import models

class quizCategory(models.Model):
    created = models.DateTimeField()
    title = models.TextField(primary_key=True) # 퀴즈 제목
    intro = models.TextField() # 퀴즈 짧은 설명
    rule = models.TextField() # 퀴즈 규칙

    class Meta:
        ordering = ['created']

class imageQuizQnA(models.Model):
    created = models.DateTimeField()
    question = models.ImageField(upload_to="%Y/%m/%d")  # media안에 몇년파일안에 몇월파일안에 몇일파일안에 이미지가 저장.
    answer = models.TextField()
    quiz_category = models.ForeignKey("quizCategory", related_name='imagequizqna', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']