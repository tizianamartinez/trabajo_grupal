def calcular_promedio(notas):
    "Recibe una lista de números (notas) y devuelve el promedio."
    "Si la lista está vacía, devuelve 0 para evitar errores."
    
    if not notas:  # Verifica si la lista está vacía
        return 0
    
    suma_total = sum(notas)
    cantidad_notas = len(notas)
    
    promedio = suma_total / cantidad_notas
    return promedio

# APORTE AGUS: Función para obtener estadísticas adicionales 
def obtener_extremos(notas):
    
    "Identifica la nota mayor y la menor de la lista utilizando max() y min()."
    if not notas:
        return None, None
    
    nota_maxima = max(notas)
    nota_minima = min(notas)
    return nota_maxima, nota_minima

#  Bloque de prueba para ejecutar el script 
if __name__ == "__main__":
    # Notas de ejemplo
    mis_notas = [8, 7, 9, 10, 6]
    
    # Llamamos a la función de promedio original
    resultado_promedio = calcular_promedio(mis_notas)
    
    # Llamamos a la nueva función de extremos (Tu aporte)
    mejor_nota, peor_nota = obtener_extremos(mis_notas)
    
    print(f"Tus notas son: {mis_notas}")
    print(f"Tu promedio final es: {resultado_promedio:.2f}")
    
    # Mostramos los resultados de tu nueva función
    print(f"La nota más alta fue un: {mejor_nota}")
    print(f"La nota más baja fue un: {peor_nota}")
    
    # Condición de aprobación
    if resultado_promedio >= 6:
        print("¡Estás aprobado! ")
    else:
        print("A recuperar... ")