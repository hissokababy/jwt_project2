from rest_framework import serializers

class LoadVideoSerializer(serializers.Serializer):
    title = serializers.CharField()
    preview = serializers.ImageField()
    video = serializers.FileField()
    duration = serializers.DurationField()
    
    
