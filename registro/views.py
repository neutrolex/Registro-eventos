from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

# Formulario para Evento
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha < timezone.now().date():
            raise ValidationError("La fecha debe ser futura.")
        return fecha

# Ver lista de eventos con búsqueda y orden
def evento_list(request):
    query = request.GET.get('q', '')
    ordenar = request.GET.get('ordenar', '')
    eventos = Evento.objects.all()

    if query:
        eventos = eventos.filter(nombre__icontains=query)

    if ordenar == 'asc':
        eventos = eventos.order_by('fecha')

    return render(request, 'registro/evento_list.html', {
        'eventos': eventos,
        'query': query,
        'ordenar': ordenar,
    })

# Crear nuevo evento
def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm()
    return render(request, 'registro/evento_form.html', {'form': form})

# Editar evento existente
def evento_update(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'registro/evento_form.html', {'form': form})

# Eliminar evento
def evento_delete(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_list')
    return render(request, 'registro/event_confirm_delete.html', {'evento': evento})
