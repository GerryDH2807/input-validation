import re

def validate_input(input_str):
    
    #Limpiar los espacios en blanco que estén en la entrada
    input_str = input_str.replace(" ", "")
    
    # Hacer la división del nombre y el primer tamaño separados por una coma
    article_name, sizes_str = input_str.split(",", 1)
    
    # Se hace la validación de los caracteres del nombre
    if not re.match("^[a-zA-Z]{2,15}$", article_name):
        return False, "Nombre del artículo no válido."
    
    # Ahora se dividen los tamaños restantes que estan divididos por comas
    sizes = sizes_str.split(",")
    
    # Se verifica que si se haya ingrasado un tamaño, de lo contrario se devolverá un mensaje
    if len(sizes) == 0:
        return False, "Debe haber al menos un tamaño."
    
    # Se verifica que no hayan más de cinco tamaños en la entrada, de lo contrario se devolverá un mensaje
    if len(sizes) > 5:
        return False, "No se permiten más de cinco tamaños."
    
    # Se inicializa el tamaño anterior como 0
    prev_size = 0
    
    # Se realiza la validación de cada tamaño
    for size in sizes:

        # Se verifica si el tamaño es un número entero
        if not size.isdigit():
            return False, f"Tamaño '{size}' no es un número entero."
        
        # Se convierte el tamaño a entero
        size_int = int(size)
        
        # Se verifica que los tamaños se encuentren en el rango 1-48
        if size_int < 1 or size_int > 48:
            return False, f"Tamaño '{size_int}' fuera del rango permitido (1-48)."
        
        # Se verifica que los tamaños estén en orden ascendente
        if size_int <= prev_size:
            return False, f"Los tamaños deben estar en orden ascendente."
        
        # Se actualiza el tamaño previo
        prev_size = size_int
    
    # Si todas las condiciones son correctas se regresará un true y a al vez un mensaje de confirmación de entrada
    return True, "Entrada válida."


# Main
input_str = "Cafe, 12, 16, 20, 24, 30"
valid, message = validate_input(input_str)
print(message)  # Salida esperada: Entrada válida.
