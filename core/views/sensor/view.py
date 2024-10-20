from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from core.models import SensorData
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class SensorDataView(View):
    template_name = 'sensores/LED.html'

    def post(self, request):
        try:
            data = json.loads(request.body)
            temperature = data.get('temperature')
            humidity = data.get('humidity')

            # Guarda los datos en la base de datos
            sensor_data = SensorData(temperature=temperature, humidity=humidity)
            sensor_data.save()

            return JsonResponse({"message": "Data saved successfully."}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get(self, request):
        led_status = LedControlView.led_status
        return JsonResponse({"led_status": led_status}, status=200)


class LedControlView(View):
    template_name = 'sensores/LED.html'

    def get(self, request):
        # Obtener el estado actual del LED desde la sesión, valor por defecto 'Apagado'
        led_status = request.session.get('led_status', 'Apagado')

        action = request.GET.get('action')

        # Actualiza el estado del LED y guarda en la sesión
        if action == 'turn_on':
            led_status = 'Encendido'
            request.session['led_status'] = led_status  # Guardar en sesión
        elif action == 'turn_off':
            led_status = 'Apagado'
            request.session['led_status'] = led_status  # Guardar en sesión

        # Renderiza el template con el estado del LED
        context = {
            'title': 'Control de LED',
            'led_status': led_status  # Usa el estado de la sesión
        }
        return render(request, self.template_name, context)


class SensoresListView(ListView):
    model = SensorData
    template_name = 'sensores/dht11.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in SensorData.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sensor DHT11'
        context['grafica_url'] = reverse_lazy('core:dashboard')
        context['list_url'] = reverse_lazy('core:category_list')
        context['api_url'] = reverse_lazy('core:sensor-data')
        context['entity'] = 'Sensor'
        return context
    # Nuevo endpoint para controlar el ESP32
