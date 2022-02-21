from django.db.models import Count, F
from django.http import HttpRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Upvote
from .permissions import CanAccessPostAPI
from .serializers import PostSerializer, DateRangeSerializer


# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [CanAccessPostAPI]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    @action(detail=True, methods=["get"])
    def upvote(self, request: HttpRequest, pk: int = None) -> Response:
        upvote = Upvote.objects.create(post=self.get_object(), author=request.user)
        upvote.save()
        return Response({"status": "post upvoted"})

    @action(detail=True, methods=["get"])
    def retract_upvote(self, request: HttpRequest, pk: int = None) -> Response:
        Upvote.objects.get(post=self.get_object(), author=request.user).delete()
        return Response({"status": "Upvote retracted"})


class AnalyticView(APIView):

    def get(self, request: HttpRequest) -> Response:
        serializer = DateRangeSerializer(data=self.request.GET)
        if serializer.is_valid():
            date_from = serializer.validated_data["date_from"]
            date_to = serializer.validated_data["date_to"]
            queryset = Upvote.objects.values('creation_date__date').annotate(
                upvotes=Count('id')).values('upvotes', date=F('creation_date__date')).order_by('date').filter(
                date__range=[date_from, date_to])

            return Response(list(queryset))
        else:
            return Response(serializer.errors, status=400)
