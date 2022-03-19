from rest_framework import serializers


class OcrViewSerializer(serializers.Serializer):
    """Serializer for proper /api/solve request."""

    puzzle_image = serializers.ImageField()


class SolveViewSerializer(serializers.Serializer):
    """Serializer for proper /api/solve request."""

    puzzle = serializers.ListField(
        min_length = 9,
        max_length = 9,
        child=serializers.ListField(
            min_length = 9,
            max_length = 9,
            child=serializers.IntegerField(
                min_value=0,
                max_value=9,
            )
        )
    )
