from webbrowser import GenericBrowser
from django.shortcuts import render
from rest_framework import generics
from .serializers import LinkSerializer
from .models import Link


from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import datetime

# Create your views here.

class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class ActiveLinkView(APIView):

    """
    Returns a list of all active (publicy accessible) links
    """

    def get(self, request):
        """
        Invoked whenever a HTTP get request is made to this VIEW.
        """
        qs = Link.public.all()
        data = LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """

    def get(self, request):
        """
        Invoked whenever a HTTP GET Request is made to this VIEW.
        """

        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = Link.public.filter(created_date__gte=seven_days_ago)
        data = LinkSerializer(qs, many=True).data

        return Response(data, status=status.HTTP_200_OK)


