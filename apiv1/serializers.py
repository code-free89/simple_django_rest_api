from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=200)
    # job = serializers.CharField(max_length=200)

    class Meta:
        fields = '__all__'