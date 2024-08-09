from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from core.forms import CategoryForm
from core.models import Category
from core.models import Product


def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # Otras funciones, filtrar ETC
    # def get_queryset(self):
    #   return Product.objects.filter(name__startswith='L')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('core:category_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de una Categoria'
        return context


