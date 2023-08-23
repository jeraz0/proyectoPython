from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html",{
        'message':"mensaje desde views",
        'subtittle':"esto es un mensaje de subtitulo",
        'productos':[
                    {'nombre':'camiseta', 'precio':1000, 'disponibilidad':True},
                    {'nombre':'camisa', 'precio':5000, 'disponibilidad':True},
                    {'nombre':'pantalón', 'precio':8000, 'disponibilidad':False}
                    ]
    })