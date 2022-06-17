from rest_framework import serializers, viewsets
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
    
class TodoView(viewsets.ModelViewSet):
    serializer_class=TodoSerializer
    queryset= Todo.objects.all()

