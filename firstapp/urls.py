from django.urls import path
from .import views

urlpatterns=[
    path('urls',views.home,name='urls'),
    path('var',views.variable,name='var'),
    path('text',views.text_analyzer,name='analyzer'),
]
