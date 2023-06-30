from django.db import models

class quizCategory(models.Model):
    created = models.DateTimeField()
    title = models.TextField() # 퀴즈 제목
    intro = models.TextField() # 퀴즈 짧은 설명
    rule = models.TextField() # 퀴즈 규칙

    class Meta:
        ordering = ['created']