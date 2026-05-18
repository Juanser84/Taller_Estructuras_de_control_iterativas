# Taller de estructuras de control iterativas

# Inicialización de variables acumuladoras y de control

total_galones = 0.0 # Acumulador para la cantidad total de galones consumidos
total_km = 0.0 # Acumulador para la cantidad total de kilómetros recorridos
mejor_rendimiento = 0.0 # Almacena el mejor rendimiento encontrado
tanqueos_validos = 0 # Contador de tanqueos con octanaje válido
tanqueos_extra = 0 # Contador de tanqueos con octanaje alto

# Lectura del primer valor para evaluar la condición de entrada

galones = float(input()) # Lectura del primer valor de galones

if galones == 0.0:
    print("No data provided.") # Caso especial: Si el primer valor es 0, no hay datos
else:
    while galones != 0.0: # Ciclo principal que se ejecuta mientras no se ingrese 0 galones
        km = float(input()) # Lectura de kilómetros recorridos
        octanaje = int(input()) # Lectura del octanaje
        
        
        
