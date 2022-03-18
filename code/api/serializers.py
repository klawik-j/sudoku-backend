from rest_framework import serializers


class OcrViewSerializer(serializers.Serializer):
    """Serializer for proper /api/solve request."""

    puzzle_image = serializers.ImageField()


class SolveViewSerializer(serializers.Serializer):
    """Serializer for proper /api/solve request."""

    puzzle = serializers.ListField(
        child=serializers.ListField(
            child=serializers.IntegerField(
                min_value=0,
                max_value=9,
            )
        )
    )
