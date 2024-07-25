from django.urls import path

from core.views.category.view import category_list

app_name = 'core'

urlpatterns = [
    path('category/list/', category_list, name='category_list'),
]
