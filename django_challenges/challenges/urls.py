from django.urls import path
from . import views
urlpatterns = [
     path('')
     path('<int:month>',views.monthly_numbers) ,
     path('<str:month>',views.monthly_challenges,name='month-challenge')
]