from rest_framework import serializers

class GraphDataSerializer(serializers.Serializer):
    inputRange1 = serializers.IntegerField()
    inputRange2 = serializers.IntegerField()