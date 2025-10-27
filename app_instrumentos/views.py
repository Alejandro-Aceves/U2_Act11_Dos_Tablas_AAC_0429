from django.shortcuts import render, get_object_or_404, redirect
from .models import Instrumento
from .forms import InstrumentoForm

def listar_instrumentos(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'listar_instrumentos.html', {'instrumentos': instrumentos})

def detalle_instrumento(request, id_instrumento):
    instrumento = get_object_or_404(Instrumento, id=id_instrumento)
    return render(request, 'detalle_instrumento.html', {'instrumento': instrumento})

def crear_instrumento(request):
    if request.method == 'POST':
        form = InstrumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_instrumentos:listar_instrumentos')
    else:
        form = InstrumentoForm()
    return render(request, 'formulario_instrumento.html', {'form': form, 'titulo': 'Crear Instrumento'})

def editar_instrumento(request, id_instrumento):
    instrumento = get_object_or_404(Instrumento, id=id_instrumento)
    if request.method == 'POST':
        form = InstrumentoForm(request.POST, request.FILES, instance=instrumento)
        if form.is_valid():
            form.save()
            return redirect('app_instrumentos:detalle_instrumento', id_instrumento=instrumento.id)
    else:
        form = InstrumentoForm(instance=instrumento)
    return render(request, 'formulario_instrumento.html', {'form': form, 'titulo': 'Editar Instrumento'})

def borrar_instrumento(request, id_instrumento):
    instrumento = get_object_or_404(Instrumento, id=id_instrumento)
    if request.method == 'POST':
        instrumento.delete()
        return redirect('app_instrumentos:listar_instrumentos')
    return render(request, 'confirmar_borrar.html', {'instrumento': instrumento})