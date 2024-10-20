from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, FormView, UpdateView

from core.forms import CategoryForm
from core.models import SensorData, LedControl
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class SensorDataView(View):

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


class ControllerLedFormView(FormView):
    form_class = CategoryForm
    template_name = 'sensores/LED.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ControllerLedUpdateView(View):
    template_name = 'sensores/LED.html'
    model = LedControl

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Obtener el registro del LED, puedes usar un ID específico o el primer registro
        led = get_object_or_404(LedControl, id=1)  # Cambia el ID según tu diseño

        # Pasar el estado actual del LED al contexto
        context = {
            'title': 'Controlador LED',
            'led_status': 'Encendido' if led.estado == 1 else 'Apagado',
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Obtener el registro del LED, puedes usar un ID específico o el primer registro
        led = get_object_or_404(LedControl, id=1)

        # Procesar la acción enviada desde el formulario
        action = request.POST.get('action')
        if action is not None:
            led.estado = 1 if action == '1' else 0  # Actualiza el estado
            led.save()  # Guardar el nuevo estado en la base de datos

        # Redirigir a la misma página para mostrar el nuevo estado
        return redirect('core:led_control')


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

class LedStatusView(View):
    def get(self, request, *args, **kwargs):
        # Obtener el registro del LED, puedes usar el ID o el primer registro
        led = get_object_or_404(LedControl, id=1)  # Cambia el ID según tu diseño

        # Devolver el estado en formato JSON
        data = {
            'estado': led.estado,  # Devolver el estado del LED (1 para encendido, 0 para apagado)
        }
        return JsonResponse(data)
