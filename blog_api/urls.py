from django.urls import path
from .views import PostList, PostDetail

app_name = "blog_api"

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name="detail-create"),
    path('', PostList.as_view(), name="list-create")
]
