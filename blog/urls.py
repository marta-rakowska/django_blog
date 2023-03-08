from django.urls import path, include
from .views import blog_list, blog_detail, blog_delete

urlpatterns = [
    path('', blog_list),
    path('<id>/', blog_detail),
    path('<id>/delete/', blog_delete)
]