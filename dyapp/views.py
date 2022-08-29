from django.shortcuts import render
from dyapp.forms import *
from dyapp.models import *
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from dynamic_forms.views import DynamicFormMixin

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = Dyforms.objects.all()
        return context


class BuildView(CreateView):
    model = Dyforms
    fields = '__all__'
    template_name = "build.html"
    success_url = "/"


class DyformDetailView(DetailView):
    model = Dyforms
    pk_url_kwarg = "form_id"
    template_name = "form_detail.html"


class DyformEditView(UpdateView):
    model = Dyforms
    fields = '__all__'
    pk_url_kwarg = "form_id"
    template_name = "form_edit.html"

    def get_success_url(self):
        return reverse('form_detail', kwargs={"form_id": self.object.pk})


class RespondView(DynamicFormMixin, CreateView):
    model = FormResponse
    fields = ['response']
    template_name = "respond.html"

    form_model = Dyforms
    form_pk_url_kwarg = "form_id"
    response_form_fk_field = "form"
    response_field = "response"

    def get_success_url(self):
        return reverse('form_detail', kwargs={"form_id": self.form_instance.pk})
