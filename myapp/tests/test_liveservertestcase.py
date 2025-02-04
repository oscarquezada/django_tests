from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from myapp.models import Producto


class LiveProductoTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.add_argument("--headless")  # Ejecuta en modo headless
        cls.selenium = webdriver.Firefox(options=options)
        cls.selenium.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        # Inserta algunos productos para la prueba
        Producto.objects.create(nombre="Impresora", precio=150.00, stock=5)
        Producto.objects.create(nombre="Monitor", precio=250.00, stock=8)

    def test_listado_productos_via_navegador(self):
        self.selenium.get(self.live_server_url + "/productos/")
        body_text = self.selenium.find_element(By.TAG_NAME, "body").text
        self.assertIn("Impresora", body_text)
        self.assertIn("Monitor", body_text)

    def test_recargar_vista_productos(self):
        self.selenium.get(self.live_server_url + "/productos/")
        self.selenium.refresh()
        body_text = self.selenium.find_element(By.TAG_NAME, "body").text
        self.assertIn("Impresora", body_text)

    def test_url_productos_valida(self):
        self.selenium.get(self.live_server_url + "/productos/")
        self.assertTrue(self.selenium.current_url.endswith("/productos/"))

    def test_producto_precio_en_lista(self):
        self.selenium.get(self.live_server_url + "/productos/")
        body_text = self.selenium.find_element(By.TAG_NAME, "body").text
        self.assertIn("150.0", body_text)

    def test_contenido_no_vacio(self):
        self.selenium.get(self.live_server_url + "/productos/")
        self.assertNotEqual(self.selenium.find_element(By.TAG_NAME, "body").text.strip(), "")
