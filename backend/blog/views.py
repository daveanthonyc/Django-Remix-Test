from .models import FeedbackForm
from .serializers import FeedbackFormSerializer
from rest_framework import viewsets

# Create your views here.
class FeedbackFormViewSet(viewsets.ModelViewSet):
    queryset = FeedbackForm.objects.all()
    serializer_class = FeedbackFormSerializer
