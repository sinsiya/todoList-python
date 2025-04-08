from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from todoList.models import ToDo
from .serializers import ToDoSerializer

# List and create To-Do items


class ToDoApiView(APIView):

    def get(self, request):
        todos = ToDo.objects.all()  # Get all To-Do items
        serializer = ToDoSerializer(todos, many=True)
        return Response({
            'statuscode': status.HTTP_200_OK,
            'title': "Data received",
            'data': serializer.data,
            'errors': '',
            'message': "To-Do items received successfully."
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)  # Create new To-Do
        if serializer.is_valid():
            serializer.save()
            return Response({
                'statuscode': status.HTTP_201_CREATED,
                'title': "To-Do Created",
                'data': serializer.data,
                'errors': '',
                'message': "To-Do item created successfully."
            }, status=status.HTTP_200_OK)
        return Response({
            'statuscode': status.HTTP_400_BAD_REQUEST,
            'title': "Validation Error",
            'data': '',
            'errors': serializer.errors,
            'message': "Failed to create To-Do item."
        }, status=status.HTTP_200_OK)

# Retrieve, update, and delete To-Do item


class ToDoDetailApiView(APIView):

    def get(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)  # Get item by ID
        serializer = ToDoSerializer(todo)
        return Response({
            'statuscode': status.HTTP_200_OK,
            'title': "Item Retrieved",
            'data': serializer.data,
            'errors': '',
            'message': "To-Do item fetched successfully."
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(todo, data=request.data)  # Update item
        if serializer.is_valid():
            serializer.save()
            return Response({
                'statuscode': status.HTTP_200_OK,
                'title': "Item Updated",
                'data': serializer.data,
                'errors': '',
                'message': "To-Do item updated successfully."
            }, status=status.HTTP_200_OK)
        return Response({
            'statuscode': status.HTTP_400_BAD_REQUEST,
            'title': "Update Error",
            'data': '',
            'errors': serializer.errors,
            'message': "To-Do item could not be updated."
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)  # Delete item by ID
        todo.delete()
        return Response({
            'statuscode': status.HTTP_204_NO_CONTENT,
            'title': "Deleted",
            'data': '',
            'errors': '',
            'message': "To-Do item deleted successfully."
        }, status=status.HTTP_200_OK)
