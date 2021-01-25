from django.shortcuts import render, get_object_or_404
from certificate.models import Certificate


def all_certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificate/all_certificates.html', {'certificates': certificates})


def certificate_detail(request, certificate_id):
    detail = get_object_or_404(Certificate, pk=certificate_id)
    return render(request, 'certificate/certificate_detail.html', {'detail': detail})
