from django.urls import path
from core.views.category.view import *

app_name = 'core'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    ]