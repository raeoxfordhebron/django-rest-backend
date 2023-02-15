from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Which model will get serialized by this class
        model = Todo
        # Which fields should be included in the output
        fields = ['id', 'subject', 'details']
