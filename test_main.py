import pytest
from main import validate_input

# Casos de prueba para validar la entrada

@pytest.mark.parametrize("input_str, expected_result", [
    
    ("Cafe,12,16,20,24,30", True),  # Sin espacios en blanco, Esperado: TRUE
    ("Leche,1", True),               # Solo un tamaño en la entrada, Esperdo: TRUE
    ("Te, 10, 20", True),           # Con espacios en blanco, Eperado:TRUE
    ("Te helado, 24, 16, 12", False),   # los tamaños no están en orden ascendente, Esperado: FALSE
    ("Cafe cortado, 8, 12, 15, 20, 25, 30", False),  # Más de cinco tamaños, Esperado: FALSE
    ("Jugo, 5, 8, 12, 16, 20, 24", False),           # Más de cinco tamaños, Esperado: FALSE
    ("T, 10", False),               # Nombre del artículo demasiado corto, Esperado: FALSE
    ("EsteEsUnNombreDeArticuloMuyLargo, 10", False), # Nombre del artículo demasiado largo, Esperado: FALSE
    ("Cafe, 0", False),             # Tamaño fuera del rango, Esperado: FALSE
    ("Te, 10.5", False),            # Tamaño no es un número entero, Esperado: FALSE
    ("Cafe, 10, 8", False),          # Tamaños no están en orden ascendente, Esperado: FALSE
    ("Te,10,20,30,40,50", False),    # Tamaños fuera del rango, Esperado: FALSE
    ("Cafe,10,20,10", False),        # Tamaños no están en orden ascendente, Esperado: FALSE
    ("Cafe con leche, 12, 16", True),# Entrada válida con espacio en el nombre del artículo, Esperado: TRUE
    ("Cafe, 12, 16, 20, 24", True),  # Entrada válida con menos de cinco tamaños, Esperado: TRUE
    ("Te, 1, 2, 3, 4, 5", True),     # Entrada válida con tamaños mínimos, Esperado: TRUE

])
def test_validate_input(input_str, expected_result):
    valid, _ = validate_input(input_str)
    assert valid == expected_result
