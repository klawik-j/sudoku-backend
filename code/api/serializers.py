from rest_framework import serializers


class OcrViewSerializer(serializers.Serializer):
    """Serializer for proper /api/solve request."""

    puzzle_image = serializers.ImageField()
