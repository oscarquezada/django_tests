# app/tests/test_views.py
from django.test import SimpleTestCase

class VistaHtmlTest(SimpleTestCase):
    def test_vista_html_status_code(self):
        response = self.client.get('/vista-html/')
        self.assertEqual(response.status_code, 200)

    def test_vista_html_contenido(self):
        response = self.client.get('/vista-html/')
        contenido = response.content.decode()
        self.assertIn("Bienvenido a la Vista HTML", contenido)
        self.assertIn("Contenido de ejemplo", contenido)

    def test_vista_html_tipo_contenido(self):
        response = self.client.get('/vista-html/')
        self.assertEqual(response['Content-Type'], "text/html; charset=utf-8")

    def test_vista_html_no_vacio(self):
        response = self.client.get('/vista-html/')
        self.assertNotEqual(response.content.strip(), b"")

    def test_vista_html_correcta_estructura(self):
        response = self.client.get('/vista-html/')
        contenido = response.content.decode()
        self.assertTrue(contenido.startswith("<html>") and contenido.endswith("</html>"))

class VistaContextoTest(SimpleTestCase):
    def test_vista_contexto_status_code(self):
        response = self.client.get('/vista-contexto/')
        self.assertEqual(response.status_code, 200)

    def test_vista_contexto_contexto_titulo(self):
        response = self.client.get('/vista-contexto/')
        # Verifica que el contexto contenga 'titulo'
        self.assertEqual(response.context['titulo'], 'Página de Contexto')

    def test_vista_contexto_contexto_mensaje(self):
        response = self.client.get('/vista-contexto/')
        self.assertEqual(response.context['mensaje'], 'Este es el mensaje del contexto.')

    def test_vista_contexto_contexto_numero(self):
        response = self.client.get('/vista-contexto/')
        self.assertEqual(response.context['numero'], 42)

    def test_vista_contexto_template_utilizado(self):
        response = self.client.get('/vista-contexto/')
        # Se asume que se utiliza el template "dummy.html"
        templates_usados = [t.name for t in response.templates if t.name is not None]
        self.assertIn("dummy.html", templates_usados)

class VistaJsonTest(SimpleTestCase):
    def test_vista_json_status_code(self):
        response = self.client.get('/vista-json/')
        self.assertEqual(response.status_code, 200)

    def test_vista_json_tipo_contenido(self):
        response = self.client.get('/vista-json/')
        self.assertEqual(response['Content-Type'], "application/json")

    def test_vista_json_valores(self):
        response = self.client.get('/vista-json/')
        data = response.json()
        self.assertEqual(data.get('status'), 'ok')
        self.assertEqual(data.get('mensaje'), 'Datos recibidos correctamente')

    def test_vista_json_estructura(self):
        response = self.client.get('/vista-json/')
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertTrue('status' in data and 'mensaje' in data)

    def test_vista_json_no_vacio(self):
        response = self.client.get('/vista-json/')
        data = response.json()
        self.assertNotEqual(len(data), 0)

class VistaRedirectTest(SimpleTestCase):
    def test_vista_redirect_status_code(self):
        response = self.client.get('/vista-redirect/')
        # El código 302 indica redirección
        self.assertEqual(response.status_code, 302)

    def test_vista_redirect_destino(self):
        response = self.client.get('/vista-redirect/')
        # Verifica que redirige a la URL '/vista-html/'
        self.assertEqual(response.url, '/vista-html/')

    def test_vista_redirect_contenido_vacio(self):
        response = self.client.get('/vista-redirect/')
        # Una redirección no debe tener contenido en la respuesta
        self.assertEqual(response.content, b"")

    def test_vista_redirect_por_metodo_get(self):
        response = self.client.get('/vista-redirect/')
        self.assertIn(response.status_code, (301, 302))

    def test_vista_redirect_consistencia(self):
        # Realiza dos peticiones y verifica que ambas redirijan al mismo destino
        response1 = self.client.get('/vista-redirect/')
        response2 = self.client.get('/vista-redirect/')
        self.assertEqual(response1.url, response2.url)
