from django.urls import path
from blogging.views import stub_view, BlogDetailView, BlogListView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
]

# list_view, detail_view