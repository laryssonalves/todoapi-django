from rest_framework.views import Response, status, APIView, Http404
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

class ApiOverview(APIView):
    def get(self, request):
        return Response({
            'list/detail': {
                'method': 'GET',
                'url': 'tasks/',
                'params': 'pk'
            },
            'create': {
                'method': 'POST',
                'url': 'tasks/',
            },
            'update': {
                'method': 'PUT',
                'url': 'tasks/<int:pk>',
            },
            'delete': {
                'method': 'DELETE',
                'url': 'tasks/<int:pk>',
            },
        })


class TaskList(APIView):
    """
    List all tasks or create a new task
    """
    def get(self, request, format=None):
        data = Task.objects.all()
        serializer = TaskSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    """
        Retrieve, update, or delete a task
    """
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
