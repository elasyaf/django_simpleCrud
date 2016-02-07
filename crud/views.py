from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from crud.models import Identitas

class CrudList(ListView):
    model = Identitas

class CrudCreate(CreateView):
    model = Identitas
    success_url = reverse_lazy('crud_list')
    fields = ['Nama', 'NIM', 'SKS']

class CrudUpdate(UpdateView):
    model = Identitas
    success_url = reverse_lazy('crud_list')
    fields = ['Nama', 'NIM', 'SKS']

class CrudDelete(DeleteView):
    model = Identitas
    success_url = reverse_lazy('crud_list')

# Index Rendering
def index(request):
    return render(request, 'crud/index.html', {})