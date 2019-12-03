from django.urls import path
from .import views

urlpatterns=[
    path('remove_punc',views.remove_punc,name='text_analyze'),
    path('analyze',views.analyze,name='text'),
]