from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def password(request):

    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    character = int(request.GET.get('length'))
    numbers = request.GET.get('numbers')
    uppercases = request.GET.get('uppercase')
    specials = request.GET.get('special')
    password = ''
    
    if numbers:
        alphabets.extend('0123456789')
    if uppercases:
        alphabets.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if specials:
        alphabets.extend('!@#$%^&*()-_?')
    
    
    for alphabet in range (character):
        password+=random.choice(alphabets)
    
    

    return render(request, 'core/password.html', {'password':password})