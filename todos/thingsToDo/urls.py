from django.urls import path
from thingsToDo.views import CView, RUDView, TasksByUser

app_name = "todos"

urlpatterns = [

    path('', CView.as_view()),
    path('<pk>', RUDView.as_view()),
    path("byUser/<pk>", TasksByUser.as_view())

]