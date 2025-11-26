from rest_framework import serializers

class ChatRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=2000, required=True, help_text="The user's new message.")
    