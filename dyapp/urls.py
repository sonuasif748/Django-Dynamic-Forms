from django.urls import path
from dyapp.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('dyform/new/',BuildView.as_view(), name="form_create"),
    path('dyform/<int:form_id>/',DyformDetailView.as_view(), name="form_detail"),
    path('dyform/<int:form_id>/edit/',DyformEditView.as_view(), name="form_edit"),
    path('dyform/<int:form_id>/response/',RespondView.as_view(), name="form_respond"),
    path('dyform/<int:form_id>/response/<int:response_id>/',RespondView.as_view(), name="response"),
]
