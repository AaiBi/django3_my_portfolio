from django.urls import path
from . import views


#app_name = 'certificate'

urlpatterns = [
    path('', views.all_certificates, name='all_certificates'),
    path('<int:certificate_id>/', views.certificate_detail, name='certificate_detail'),
]
