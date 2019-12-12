from django.shortcuts import render

def portal(request):
    return render(request, 'portal_page.html')
