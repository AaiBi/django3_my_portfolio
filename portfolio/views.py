from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html')


# def certification_detail(request, certification_id):
#     details = get_object_or_404(Certificate, pk=certification_id)
#     return render(request, 'portfolio/certification_detail.html', {'details': details})
