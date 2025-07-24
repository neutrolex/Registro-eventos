from django.urls import reverse
from .models import Event

class TestEventoDeleteView(TestCase):
    def setUp(self):
        self.evento = Evento.objects.create(
            nombre="Prueba",
            fecha="2099-12-31",
            ubicacion="Lugar",
            organizador="Admin"
        )

    def test_eliminar_evento(self):
        url = reverse('evento_delete', args=[self.evento.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('evento_list'))
        
#python manage.py test registro <-- colocar esto para el test