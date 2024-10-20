from django.urls import path
from core.views.category.view import *
from core.views.dashboard.view import *
from core.views.sensor.view import *

app_name = 'core'

urlpatterns = [
    # Category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    #Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #Sensores
    path('api/sensor-data', SensorDataView.as_view(), name='sensor-data'),
    path('sensores/list/', SensoresListView.as_view(), name='sensores_list'),
    path('led/', ControllerLedUpdateView.as_view(), name='led_control'),
    path('led/status/', LedStatusView.as_view(), name='led_status'),
]


