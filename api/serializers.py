from rest_framework import serializers


class SentenceSerializer(serializers.Serializer):
    sentence = serializers.CharField()
