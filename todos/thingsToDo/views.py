from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from thingsToDo.models import Todos 
from thingsToDo.serializers import TodosSerializer

# Create your views here.
class CView(ListCreateAPIView):

    """
    ListCreateAPIView maneja GetAll y POST 
    """
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

    def perform_create(self, serializer):
        serializer.save()


class RUDView(RetrieveUpdateDestroyAPIView):

    """
    RetrieveUpdateDestroyAPIView maneja GET, PUT y DELETE
    """

    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

class TasksByUser(ListAPIView):

    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

    def get_queryset(self):
        return Todos.objects.filter(user=self.kwargs['pk'])