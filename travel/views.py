from django.shortcuts import render
from travel import models
from django.http import JsonResponse

def get_users(request):
    all_users = models.TCTUsers.objects.all()
    list_of_users = []
    for one_user in all_users:
        list_of_users.append({
            'id':one_user.id,
            'full_name':one_user.full_name,
            'contact':one_user.contact,
            'email':one_user.email
        })
    return render(request, 'homepage.html', {})
    return JsonResponse({
        'data':list_of_users
    })


# def dest

# Create your views here.
