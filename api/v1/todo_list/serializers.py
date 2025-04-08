from rest_framework import serializers
from todoList.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title is required.")
        return value
