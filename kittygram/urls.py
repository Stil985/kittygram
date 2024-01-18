from django.urls import path

from cats.views import cat_list, cat_detail, APICat, APICatDetail

urlpatterns = [
   path('cats/', cat_list),
   path('cats/<int:pk>/', cat_detail),
   path('api/cats/', APICat.as_view()),
   path('api/cats/<int:pk>/', APICatDetail.as_view()),
]
