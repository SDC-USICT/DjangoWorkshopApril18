from django.contrib import admin
from django.urls import path
from answers.views import index, ask_questions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', index),
    path('ask/questions', ask_questions)
]
