from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.


# class PruebaCreteView(CreateView):

#     template_name = "home/add.html"
#     model = Prueba 
#     fields = ['titulo', 'subtitulo', 'cantidad']
#     success_url = '/'


class IndexView(TemplateView):
    template_name= 'home/home.html'


class PruebaListView(ListView):
    template_name =  'home/lista.html'
    queryset = ['A','B','C']
    context_object_name =  'lista_prueba'


