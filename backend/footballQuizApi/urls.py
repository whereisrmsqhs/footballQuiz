from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from quiz.api import QuizCategoryList, QuizCategoryDetail, imageQuizQnAList, imageQuizQnADetail
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Swagger Study API",
        default_version="v1",
        description="Swagger Study를 위한 API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(name="test", email="dhkep03@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("api/", include('post.urls')),
    path("quizCategory_list", QuizCategoryList.as_view(), name="quizCategory_list"),
    path("quizCategory_list/<str:title>", QuizCategoryDetail.as_view(), name="quizCategory_list"),
    path("quizCategory_list/<str:quiz_category>/imageQuiz_list", imageQuizQnAList.as_view(), name="imageQuizAna_list"),
    path("quizCategory_list/<str:title>/imageQuiz_list/<int:id>", imageQuizQnADetail.as_view(), name="imageQuizAna_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    ]
