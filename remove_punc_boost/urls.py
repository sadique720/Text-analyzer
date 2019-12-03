from django.urls import path
from .import views

urlpatterns=[
    path('remove_punc',views.remove_punc,name='remove_punc'),
    path('analyze',views.analyze,name='analyze')
]