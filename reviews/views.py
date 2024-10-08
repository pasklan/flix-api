from reviews.models import Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from reviews.serializers import ReviewSerializer
from reviews.permissions import ReviewPermissionClass


class ReviewCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, ReviewPermissionClass)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
