from django.test import TestCase
from myapp.models import Producto, Cliente, Pedido

class ProductoTestCase(TestCase):

    def setUp(self):
        self.prod1 = Producto.objects.create(nombre="Laptop", precio=999.99, stock=10)
        Producto.objects.create(nombre="Tablet", precio=499.99, stock=20)

    def test_insercion_producto(self):
        prod = Producto.objects.create(nombre="Smartphone", precio=299.99, stock=15)
        self.assertIsNotNone(prod.id)

    def test_actualizacion_producto(self):
        self.prod1.precio = 1099.99
        self.prod1.save()
        self.prod1.refresh_from_db()
        self.assertEqual(self.prod1.precio, 1099.99)

    def test_busqueda_producto(self):
        prod = Producto.objects.get(nombre="Laptop")
        self.assertEqual(prod.precio, 999.99)

    def test_eliminacion_producto(self):
        prod = Producto.objects.get(nombre="Tablet")
        prod.delete()
        with self.assertRaises(Producto.DoesNotExist):
            Producto.objects.get(nombre="Tablet")

    def test_listado_productos(self):
        productos = Producto.objects.all()
        self.assertTrue(productos.count() >= 2)

class ClienteTestCase(TestCase):
    urls = 'app.tests.test_modelos_testcase'  # Indica el módulo donde se encuentran las URLs de prueba

    def setUp(self):
        self.cli1 = Cliente.objects.create(nombre="Ana", apellido="García", email="ana@example.com")
        Cliente.objects.create(nombre="Luis", apellido="Martínez", email="luis@example.com")

    def test_insercion_cliente(self):
        cli = Cliente.objects.create(nombre="Carlos", apellido="Sánchez", email="carlos@example.com")
        self.assertIsNotNone(cli.id)

    def test_actualizacion_cliente(self):
        self.cli1.apellido = "López"
        self.cli1.save()
        self.cli1.refresh_from_db()
        self.assertEqual(self.cli1.nombre_completo(), "Ana López")

    def test_busqueda_cliente(self):
        cli = Cliente.objects.get(email="luis@example.com")
        self.assertEqual(cli.nombre, "Luis")

    def test_eliminacion_cliente(self):
        cli = Cliente.objects.get(email="luis@example.com")
        cli.delete()
        with self.assertRaises(Cliente.DoesNotExist):
            Cliente.objects.get(email="luis@example.com")

    def test_vista_listar_clientes(self):
        response = self.client.get('/clientes/')
        self.assertEqual(response.status_code, 200)
        contenido = response.content.decode()
        self.assertIn("Ana García", contenido)
        self.assertIn("Luis Martínez", contenido)

class PedidoTestCase(TestCase):

    def setUp(self):
        self.pedido1 = Pedido.objects.create(descripcion="Pedido de oficina")
        Pedido.objects.create(descripcion="Pedido para tienda")

    def test_insercion_pedido(self):
        ped = Pedido.objects.create(descripcion="Pedido de laboratorio")
        self.assertIsNotNone(ped.id)

    def test_actualizacion_pedido(self):
        self.pedido1.descripcion = "Pedido actualizado de oficina"
        self.pedido1.save()
        self.pedido1.refresh_from_db()
        self.assertEqual(self.pedido1.descripcion, "Pedido actualizado de oficina")

    def test_busqueda_pedido(self):
        ped = Pedido.objects.get(descripcion="Pedido para tienda")
        self.assertEqual(ped.descripcion, "Pedido para tienda")

    def test_eliminacion_pedido(self):
        ped = Pedido.objects.get(descripcion="Pedido para tienda")
        ped.delete()
        with self.assertRaises(Pedido.DoesNotExist):
            Pedido.objects.get(descripcion="Pedido para tienda")

    def test_listado_pedidos(self):
        pedidos = Pedido.objects.all()
        self.assertTrue(pedidos.count() >= 2)
