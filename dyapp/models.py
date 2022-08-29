from django.db import models
from dynamic_forms.models import FormField, ResponseField
from datetime import datetime


class Dyforms(models.Model):
    form_name = models.CharField(max_length=100)
    form_number = models.BigIntegerField(null=True,blank=True)
    form_id = models.BigIntegerField(null=True,blank=True)
    form_time = models.DateTimeField(auto_now=True,null=True,blank=True)

    form = FormField()

    def __str__(self):
        return "Form #{}: {}".format(self.pk, self.form_name)


class FormResponse(models.Model):
    form = models.ForeignKey(Dyforms, on_delete=models.CASCADE)
    response = ResponseField()


