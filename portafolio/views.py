from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def home(request):
    return render(request, "pages/home.html")

def sobre_mi(request):
    return render(request, 'pages/sobre_mi.html')

def proyectos(request):
    # Aquí debes obtener tus proyectos desde la base de datos o de otra fuente
    proyectos = [
        {
            'titulo': 'Proyecto 1',
            'descripcion': 'Descripción del proyecto 1',
            'imagen': 'ruta/a/la/imagen1.jpg',
            'url': 'https://www.ejemplo.com/proyecto1',
        },
        # ... más proyectos
    ]
    return render(request, 'pages/proyectos.html', {'proyectos': proyectos})

def contacto(request):
    # Aquí puedes manejar el envío del formulario de contacto
    if request.method == 'POST':
        # Procesa los datos del formulario
        pass
    return render(request, 'pages/contacto.html')