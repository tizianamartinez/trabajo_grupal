
def saludo_final(nombre):
    mensaje = "¡Hola " + nombre + "! Esta es la parte de Tiziana."
    return mensaje

def calcular_promedio(notas):
    """
    Recibe una lista de números (notas) y devuelve el promedio.
    Si la lista está vacía, devuelve 0 para evitar errores.
    """
    if not notas:  # Verifica si la lista está vacía
        return 0
    
    suma_total = sum(notas)
    cantidad_notas = len(notas)
    
    promedio = suma_total / cantidad_notas
    return promedio


# --- Bloque de prueba para ejecutar el script ---
if __name__ == "__main__":
    # Imagina que estas son tus notas de los parciales
    mis_notas = [8, 7, 9, 10, 6]
    
    # Llamamos a la función
    resultado_promedio = calcular_promedio(mis_notas)
    
    print(f"Tus notas son: {mis_notas}")
    print(f"Tu promedio final es: {resultado_promedio:.2f}")
    
    # Un extra: te avisa si aprobaste (con 6 o más)
    if resultado_promedio >= 6:
        print("¡Estás aprobado! 🎉")
    else:
        print("A recuperar... 📚")
 
