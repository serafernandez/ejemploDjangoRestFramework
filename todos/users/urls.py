from django.urls import path
from users.views import CView, RUDView

app_name = "users"

urlpatterns = [
    path('', CView.as_view()),
    path('<pk>', RUDView.as_view())
]