from django.urls import path
from core.views.category.view import *
from core.views.proceso.view import *
from core.views.dashboard.view import *

app_name = 'core'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('proceso/list/', ProcesoListView.as_view(), name='proceso_list'),
    path('proceso/add/', ProcesoCreateView.as_view(), name='proceso_create'),
    path('dashboard/ver/', DashboardView.as_view(), name='Inicio'),
]
