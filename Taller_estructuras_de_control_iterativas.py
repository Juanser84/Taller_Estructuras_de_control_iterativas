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
        
# Ciclo anidado para la validación del octanaje
        
        while octanaje < 81 or octanaje > 98: # Validación del octanaje
            print("OCTANAJE INVALIDO") # Mensaje de error para octanaje inválido
            octanaje = int(input()) # Lectura del octanaje nuevamente
            
        rendimiento_actual = km / galones # Cálculo del rendimiento actual
        
        if rendimiento_actual > mejor_rendimiento: # Verificación del mejor rendimiento histórico
            mejor_rendimiento = rendimiento_actual # Actualización del mejor rendimiento
            
        total_galones += galones # Acumulación de galones
        total_km += km # Acumulación de kilómetros
        tanqueos_validos += 1 # Incremento del contador de tanqueos válidos
        
        if octanaje >= 90: # Verificación de gasolina de alto octanaje (Extra)
            tanqueos_extra += 1 # Incremento del contador de tanqueos con octanaje alto
            
        galones = float(input()) # Lectura del siguiente registro de galones
        
        
