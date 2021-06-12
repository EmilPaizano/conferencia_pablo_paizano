from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Conferencista,Participante
# Create your views here.

def index(request):
    return render(request, 'registro/index.html')


def participantes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        p = Participante(nombre=nombre, apellido=apellido, correo=correo, twitter=twitter)
        p.save()

        # msj = f'El participante {nombre} {apellido} ha sido registrado con éxito.'

        # Codigo para enviar un mensaje a un grupo de telegram

        # try:
        #     bot.send_message(chat_id=GROUP_ID, text=msj)
        # except Exception as e:
        #     msj += f'<br/><strong>{e}</strong>'
        
        # messages.add_message(request, messages.INFO, msj)

        # return JsonResponse({
        #     'nombre': nombre,
        #     'apellido': apellido,
        #     'correo': correo,
        #     'twitter': twitter,
        #     'OK': True,
        #     'msj': 'El participante ha sido registrado con éxito'
        # })

        # ctx = {
        #     'participantes': Participante.objects.all().order_by('nombre')
        # }

        # return HttpResponse('El participante ha sido registrado')
        # return render(request, 'registro/participantes.html', ctx)
    
    # Metodo GET, PUT, PATCH, DELETE

    # La primera consulta: select * from participantes order by nombre desc
    # Realizar un Queryset con el ORM de Django
    activo = 'participantes'
    q = request.GET.get('q')

    if q:
        data = Participante.objects.filter(nombre__startswith=q).order_by('nombre')

        '''
            select * 
            from participantes
            where nombre like 'n%'
        '''
    else:
        data = Participante.objects.all().order_by('nombre')

    ctx = {
        'activo': activo,
        'participantes': data,
        'q': q
    }

    return render(request, 'registro/participantes.html', ctx)


def eliminar_participante(request, id):
    Participante.objects.get(pk=id).delete()
    return redirect(reverse('participantes'))


def editar_participante(request, id):
    par = get_object_or_404(Participante, pk=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        par.nombre = nombre
        par.apellido = apellido
        par.correo = correo
        par.twitter = twitter
        par.save()

    #par = Participante.objects.get(pk=id)    
    data = Participante.objects.all().order_by('nombre')

    ctx = {
        'activo': 'participantes',
        'participantes': data,
        'p': par
    }

    return render(request, 'registro/participantes.html', ctx)

def conferencistas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        experiencia = request.POST.get('experiencia')

        p = Conferencista(nombre=nombre, apellido=apellido, experiencia=experiencia)
        p.save()

        # msj = f'El conferencista {nombre} {apellido} ha sido registrado con éxito.'

        # # Codigo para enviar un mensaje a un grupo de telegram

        # try:
        #     bot.send_message(chat_id=GROUP_ID, text=msj)
        # except Exception as e:
        #     msj += f'<br/><strong>{e}</strong>'

        # messages.add_message(request, messages.INFO, msj)
    activo = 'conferencistas'
    q = request.GET.get('q')

    if q:
        data = Conferencista.objects.filter(nombre__startswith=q).order_by('nombre')

    else:
        data = Conferencista.objects.all().order_by('nombre')

    ctx = {
        'activo': activo,
        'conferencistas': data,
        'q': q
    }

    return render(request, 'registro/conferencistas.html', ctx)


def eliminar_conferencista(request, id):
    Conferencista.objects.get(pk=id).delete()
    return redirect(reverse('conferencistas'))