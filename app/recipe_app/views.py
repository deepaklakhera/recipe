from django.shortcuts import render
from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from core.models import Tag
from . serializers import TagSerializer

class TagviewSet(viewsets.GenericViewSet,mixins.ListModelMixin):

    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    queryset=Tag.objects.all()
    serializer_class=TagSerializer

    def get_queryset(self):
        
        return self.queryset.filter(user=self.request.user).order_by('-name')

    

