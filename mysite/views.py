from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def acceuil(request):
    return render(request,'acceuil.html' )


# @login_required
# def index2(request):
#     if request.user.is_authenticated:
#         request.session['username'] = request.user.username
#     return render(request, 'acceuil.html')