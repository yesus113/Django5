from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from core.forms import ProcesoForm
from core.models import Procesos


def proceso_list(request):
    data = {
        'title': 'Listado de Procesos',
        'procesos': Procesos.objects.all()
    }
    return render(request, 'proceso/list.html', data)


class ProcesoListView(ListView):
    model = Procesos
    template_name = 'proceso/list.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Procesos.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # Otras funciones, filtrar ETC
    # def get_queryset(self):
    #   return Product.objects.filter(name__startswith='L')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Procesos'
        return context

class ProcesoCreateView(CreateView):
    model = Procesos
    form_class = ProcesoForm
    template_name = 'proceso/create.html'
    success_url = reverse_lazy('core:proceso_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de un proceso'
        return context


