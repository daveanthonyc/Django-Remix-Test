from rest_framework import serializers
from .models import FeedbackForm

class FeedbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackForm
        fields = "__all__"