from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleDoAll, ArticleRetriveView
urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleRetriveView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('doall/<pk>/', ArticleDoAll.as_view()),
]
