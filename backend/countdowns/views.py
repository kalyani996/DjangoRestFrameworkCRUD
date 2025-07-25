from django.shortcuts import render
from .serializers import CountdownSerializer
from .models import Countdown
from rest_framework import generics
from django.shortcuts import get_object_or_404
from api.mixins import IsStaffEditorPermission, UserQueryMixin
# Create your views here.

class CountdownListCreateAPIView(IsStaffEditorPermission,generics.ListCreateAPIView):
    queryset = Countdown.objects.all()
    serializer_class = CountdownSerializer
    def perform_create(self, serializer):
            print(serializer.validated_data)
            name = serializer.validated_data.get('name')
            targetTime = serializer.validated_data.get('target_time') or None
            if targetTime is None:
                raise serializer.ValidationError({"target_time": "Target time is required for countdown."})
            serializer.save(user=self.request.user) #form.save() model.save()
cowntdown_list_create_view = CountdownListCreateAPIView.as_view()

class CountdownDetailAPIView(IsStaffEditorPermission,generics.RetrieveAPIView):
    queryset = Countdown.objects.all()
    serializer_class = CountdownSerializer
cowntdown_detail_view = CountdownDetailAPIView.as_view()

