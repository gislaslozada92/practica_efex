from rest_framework import serializers


class StudentInputSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    grade = serializers.IntegerField()
    phone = serializers.CharField()
    email = serializers.CharField()


class StudentOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth = serializers.DateField()
    grade = serializers.IntegerField()
    phone = serializers.CharField()
    email = serializers.CharField()
