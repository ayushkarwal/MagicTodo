from rest_framework import serializers
from .models import Task
from datetime import datetime

class TaskSerializer(serializers.ModelSerializer):
    # due_in = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = "__all__"
    
    # def get_due_in(self, obj):
    #     import pdb; pdb.set_trace()
    #     currentdt = ''