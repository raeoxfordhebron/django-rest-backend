from .models import Todo
from rest_framework import serializers

# Serializer is just for pretty JSON objects
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Which model will get serialized by this class
        model = Todo 
        # Which fields should be included in the output
        # SQL tables always have an ID field, subject and details were created in our model
        fields = {'id', 'subject', 'details'}
