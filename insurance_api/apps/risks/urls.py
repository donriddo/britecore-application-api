from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('risk_type', views.RiskTypeList.as_view(), name='risk-type-list'),
    path('risk', views.RiskList.as_view(), name='risk-list'),
    path('risk_type/<int:pk>', views.RiskTypeDetail.as_view(), name='risk-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
