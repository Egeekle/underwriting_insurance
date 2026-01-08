import sys
import os
import pytest

# Add src/infrastructure to path so we can import the module
# assuming test/ is at root and src/infrastructure is at src/infrastructure
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/infrastructure')))

try:
    from advanced_broker_vehicular import clasificar_intencion
except ImportError:
    # Fallback if running from a different context or if structure differs
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from src.infrastructure.advanced_broker_vehicular import clasificar_intencion

def test_intencion_saludo():
    assert clasificar_intencion("Hola, buenos días") == "SALUDO"
    assert clasificar_intencion("Gracias") == "SALUDO"
    assert clasificar_intencion("Chau") == "SALUDO"

def test_intencion_emergencia():
    assert clasificar_intencion("Choqué mi auto") == "EMERGENCIA"
    assert clasificar_intencion("Me robaron el carro") == "EMERGENCIA"
    assert clasificar_intencion("Necesito una grúa") == "EMERGENCIA"

def test_intencion_consulta():
    assert clasificar_intencion("Quiero saber el precio del seguro") == "CONSULTA"
    assert clasificar_intencion("Comparar Rimac y Pacífico") == "CONSULTA"
    assert clasificar_intencion("¿Qué cubre la póliza?") == "CONSULTA"
