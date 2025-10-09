from django.shortcuts import render


def Dashboard(request):
    return render(request, 'OSCA_WEB_APP/dashboard.html')

