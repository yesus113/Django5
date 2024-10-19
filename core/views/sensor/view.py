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
        action = request.GET.get('action')  # Obtén el valor del botón presionado

        # Determina si encender o apagar el LED
        if action == 'turn_on':
            value = 1
            command = 'turn_on_led'
        elif action == 'turn_off':
            value = 0
            command = 'turn_off_led'
        else:
            value = 0  # Valor por defecto o manejar error
            command = 'Accion invalida'

        # Enviar comando para encender o apagar el LED
        data_to_send = {
            "command": command,
            "value": value
        }
        return JsonResponse(data_to_send, status=200)


class LedControlView(View):
    template_name = 'sensores/LED.html'

    def get(self, request):
        # Obtener el estado actual del LED desde alguna fuente (ejemplo: variable o base de datos)
        action = request.GET.get('action')
        if action == 'turn_on':
            led_status = 'Encendido'
        elif action == 'turn_off':
            led_status = 'Apagado'
        else:
            led_status = 'Desconocido'  # Valor por defecto si no se envía acción

        # Renderiza el template con el estado del LED
        context = {
            'title': 'Control de LED',
            'led_status': led_status  # Aquí se almacena el estado actual del LED
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
