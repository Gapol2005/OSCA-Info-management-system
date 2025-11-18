from django.shortcuts import render


def Dashboard(request):
    return render(request, 'dashboard_admin.html')

def Registration_Category(request):
    return render(request, 'Registration_Category.html')

