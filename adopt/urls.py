from django.urls import path

from . import views

app_name = 'adopt'
urlpatterns = [
        path('', views.index),
        path('<int:pet_id>/', view.detail, name = 'detail')

]


