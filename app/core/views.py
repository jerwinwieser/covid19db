from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class IndexView(TemplateView):
	template_name = 'core/index.html'
