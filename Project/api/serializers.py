#createing serializer
from rest_framework import serializers
from api.models import Client,User,Project

#for clients
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'client_name', 'created_by', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_name']


class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['project_id', 'project_name', 'client', 'users', 'created_at', 'created_by']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['client'] = instance.client.client_name  # Include client name in the response
        representation['users'] = UserSerializer(instance.users, many=True).data  # Include detailed user info
        return representation

