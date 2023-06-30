from django.contrib import admin
from django.urls import path, include
from quiz.api import QuizCategoryList, QuizCategoryDetail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('post.urls')),
    path("api/quizCategory_list", QuizCategoryList.as_view(), name="quizCategory_list"),
    path("api/quizCategory_list/<str:title>", QuizCategoryDetail.as_view(), name="quizCategory_list"),
]
