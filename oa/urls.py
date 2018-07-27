from django.urls import path
from . import views

# start with blog
urlpatterns = [
    # http://localhost:8000/oas/
    path('', views.article_list, name='article_list'),
    path('<int:article_pk>', views.article_detail, name="article_detail"),
    path('type/<int:err_type_pk>', views.article_with_type, name="article_with_type"),
    path('date/<int:year>/<int:month>', views.article_with_date, name="article_with_date"),
]