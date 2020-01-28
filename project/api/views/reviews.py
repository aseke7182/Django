from rest_framework import generics, filters
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import Http404
from api.serializers import *
from api.models import *


class AllReviews(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class OwnReview(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        reviews = Review.objects.all()
        queryset = reviews.filter(reviewer=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)


class ReviewInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        reviews = Review.objects.all()
        queryset = reviews.filter(reviewer=self.request.user)
        return queryset


class AllCompany(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
