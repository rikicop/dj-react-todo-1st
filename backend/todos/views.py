from rest_framework import generics
from .models import Todo, Constante
from .serializers import TodoSerializer, ConstanteSerializer

class ListTodo(generics.ListAPIView):
    #p = Todo(title='Cien Años de Soledad', body='Cuento de Gabriel García Marquez')
    #p.save()
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ListConstante(generics.ListAPIView):
    a=34
    b=56
    c=a+b
    p = Constante.objects.get_or_create(valor=c, descripcion='Suma Simple')
    #p.valor = 299000
    queryset = Constante.objects.all()
    serializer_class = ConstanteSerializer

