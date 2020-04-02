from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from ..models import Article
from .serializers import ArticleSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetriveView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDoAll(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
