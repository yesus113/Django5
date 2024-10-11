from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Avg, FloatField
from django.db.models.functions import Coalesce, Cast
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from core.models import SensorData
from random import randint


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'Report_dht11_months':
                data = self.Report_dht11_months()
            elif action == 'get_graph_online':
                last_record = SensorData.objects.latest('id')  # Obtener el último registro
                data = {'y': last_record.temperature, 'h': last_record.humidity}  # Enviar la temperatura del último registro
                print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
            # data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def Report_dht11_months(self):
        temperature_avg = []
        humidity_avg = []

        year = datetime.now().year
        for m in range(1, 13):
            # Promedio de temperatura
            temp_promedio = SensorData.objects.filter(datetime__year=year, datetime__month=m).aggregate(
                avg_temperature=Coalesce(Avg(Cast('temperature', FloatField())), 0.0)  # Asegurando que sea float
            )
            temperature_avg.append(temp_promedio['avg_temperature'])

            # Promedio de humedad
            hum_promedio = SensorData.objects.filter(datetime__year=year, datetime__month=m).aggregate(
                avg_humidity=Coalesce(Avg(Cast('humidity', FloatField())), 0.0)  # Asegurando que sea float
            )
            humidity_avg.append(hum_promedio['avg_humidity'])

        return temperature_avg, humidity_avg

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Panel'] = 'Panel de administración'
        context['temperature_avg'], context['humidity_avg'] = self.Report_dht11_months()
        return context
