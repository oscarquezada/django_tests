from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Cliente, Reserva, Producto


# ============================
# VISTAS PARA PRUEBAS DE TESTCASE
# (Consultas a la base de datos)
# ============================

def listar_clientes(request):
    """Vista que retorna una lista de clientes (TestCase)."""
    clientes = Cliente.objects.all()
    nombres = ", ".join([cli.nombre_completo() for cli in clientes])
    return HttpResponse(nombres)

def listar_pedidos(request):
    """Vista simple para retornar pedidos (TestCase)."""
    # Aquí se podría extender según las necesidades
    return HttpResponse("Vista de pedidos")

# ============================
# VISTAS PARA PRUEBAS DE TRANSACTIONTESTCASE
# (Vistas que consultan modelos con restricciones)
# ============================

def listar_reservas(request):
    """Vista que retorna la lista de reservas (TransactionTestCase)."""
    reservas = Reserva.objects.all()
    nombres = ", ".join([reserva.nombre for reserva in reservas])
    return HttpResponse(nombres)

# ============================
# VISTAS PARA PRUEBAS LIVE SERVER (LiveServerTestCase / LiveTransactionTestCase)
# ============================

def listar_productos(request):
    """Vista que retorna una lista en HTML de productos para pruebas end-to-end."""
    productos = Producto.objects.all()
    html = "<ul>" + "".join([f"<li>{p.nombre} - {p.precio}</li>" for p in productos]) + "</ul>"
    return HttpResponse(html)


# app/views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# --- Vista que retorna HTML estático ---
def vista_html(request):
    html = "<html><body><h1>Bienvenido a la Vista HTML</h1><p>Contenido de ejemplo.</p></body></html>"
    return HttpResponse(html)

# --- Vista que retorna un contexto (usando render) ---
def vista_contexto(request):
    contexto = {
        'titulo': 'Página de Contexto',
        'mensaje': 'Este es el mensaje del contexto.',
        'numero': 42
    }
    # Se asume que existe un template llamado "dummy.html"
    return render(request, 'dummy.html', contexto)

# --- Vista que retorna JSON ---
def vista_json(request):
    data = {
        'status': 'ok',
        'mensaje': 'Datos recibidos correctamente'
    }
    return JsonResponse(data)

# --- Vista de redirección ---
def vista_redirect(request):
    # Redirige a la vista HTML
    return redirect('/vista-html/')
