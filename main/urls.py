from django.urls import path
from main import views

urlpatterns  = [
    path('',views.index, name ='index' ),
    path('article/<int:pk>',views.article,name = 'get_article')
]