"""
URL configuration for Software_design project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views

# 这是一个URL配置文件，用于配置URL和视图之间的映射关系
urlpatterns = [
    path('admin/', admin.site.urls),
    path('view_train/', views.view_train, name='view_train'),
    path('split_sentences/', views.split_sentences, name='split_sentences'),
    path('get_words/', views.get_words, name='get_words'),
    path('GetSubmission/', views.get_submission, name='get_submission'),
    path('GetTask/', views.get_task, name='get_task'),
    path('translate_sentence/', views.translate_sentence, name='translate_sentence'),
    path('annotation_by_llm/', views.annotation_by_llm, name='annotation_by_llm'),
    path('GetPos/', views.get_pos_data, name='get_pos_data'),
    path('GetEntity/', views.get_entity_data, name='get_entity_data'),
    path('update_case/', views.update_case, name='update_case'),
    path('export_data/', views.export_data, name='export_data'),
    path('split_words/', views.split_words, name='split_words'),
]
