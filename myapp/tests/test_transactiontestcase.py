from django.test import TransactionTestCase
from django.db import IntegrityError
from myapp.models import Usuario, Reserva, Categoria


class UsuarioTransactionTest(TransactionTestCase):

    def setUp(self):
        Usuario.objects.create(username="user1", email="user1@example.com")


    def test_eliminacion_usuario(self):
        user = Usuario.objects.get(username="user1")
        user.delete()
        with self.assertRaises(Usuario.DoesNotExist):
            Usuario.objects.get(username="user1")
            
    def test_insercion_usuario(self):
        user = Usuario.objects.create(username="user2", email="user2@example.com")
        self.assertIsNotNone(user.id)

    def test_actualizacion_usuario(self):
        user = Usuario.objects.get(username="user1")
        user.email = "nuevo@example.com"
        user.save()
        user.refresh_from_db()
        self.assertEqual(user.email, "nuevo@example.com")

    def test_busqueda_usuario(self):
        user = Usuario.objects.get(username="user1")
        self.assertEqual(user.email, "user1@example.com")

    def test_restriccion_unicidad_usuario(self):
        with self.assertRaises(IntegrityError):
            Usuario.objects.create(username="user3", email="user1@example.com")

# --- Reserva (incluye prueba vía vista) ---
class ReservaTransactionTest(TransactionTestCase):
    urls = 'app.tests.test_transacciones'  # Define el módulo de URLs de prueba

    def setUp(self):
        self.reserva = Reserva.objects.create(nombre="Reserva A")

    def test_insercion_reserva(self):
        res = Reserva.objects.create(nombre="Reserva B")
        self.assertIsNotNone(res.id)

    def test_actualizacion_reserva(self):
        self.reserva.confirmar()
        self.reserva.refresh_from_db()
        self.assertTrue(self.reserva.confirmada)

    def test_busqueda_reserva(self):
        res = Reserva.objects.get(nombre="Reserva A")
        self.assertEqual(res.nombre, "Reserva A")

    def test_eliminacion_reserva(self):
        res = Reserva.objects.get(nombre="Reserva A")
        res.delete()
        with self.assertRaises(Reserva.DoesNotExist):
            Reserva.objects.get(nombre="Reserva A")

    def test_vista_listar_reservas(self):
        response = self.client.get('/reservas/')
        self.assertEqual(response.status_code, 200)
        contenido = response.content.decode()
        self.assertIn("Reserva A", contenido)

# --- Categoria ---
class CategoriaTransactionTest(TransactionTestCase):

    def setUp(self):
        Categoria.objects.create(nombre="Tecnología")

    def test_insercion_categoria(self):
        cat = Categoria.objects.create(nombre="Cocina")
        self.assertIsNotNone(cat.id)

    def test_actualizacion_categoria(self):
        cat = Categoria.objects.get(nombre="Tecnología")
        cat.nombre = "Electrónica"
        cat.save()
        cat.refresh_from_db()
        self.assertEqual(cat.nombre, "Electrónica")

    def test_busqueda_categoria(self):
        cat = Categoria.objects.get(nombre="Tecnología")
        self.assertEqual(cat.nombre, "Tecnología")

    def test_eliminacion_categoria(self):
        cat = Categoria.objects.get(nombre="Tecnología")
        cat.delete()
        with self.assertRaises(Categoria.DoesNotExist):
            Categoria.objects.get(nombre="Tecnología")

    def test_restriccion_unicidad_categoria(self):
        with self.assertRaises(Exception):  # Puede ser IntegrityError u otra excepción
            Categoria.objects.create(nombre="Cocina")
            Categoria.objects.create(nombre="Cocina")
