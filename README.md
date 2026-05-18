# 🏍️ Laboratorio 1: Telemetría de Motocicleta (Ciclo While)

¡Hola! Este es mi repositorio con la solución al primer taller de programación sobre estructuras de control iterativas (ciclos `while`).

El programa simula el sistema de telemetría de una moto de gama alta para procesar los datos de los tanqueos, calcular qué tan eficiente es el motor y revisar qué tipo de gasolina se usó.

## 📌 ¿Cómo funciona el código?
El programa pide tres datos en orden por cada tanqueo:
1. **Galones** (Si pones `0` al principio, te dice que no hay datos. Si lo pones después de meter viajes, el programa se cierra y te da los resultados).
2. **Kilómetros recorridos**.
3. **Octanaje** (Solo acepta números entre 81 y 98. Si metes uno malo, te frena y te dice `OCTANAJE INVALIDO` hasta que pongas uno correcto).

## 🛠️ Reglas del taller que se cumplieron:
* **Entradas mudas:** No usé textos descriptivos dentro de los `input()`, la consola arranca en blanco.
* **Control de flujo limpio:** No usé ni `break` ni `continue`. Todo el ciclo se controla con condiciones booleanas normales.
* **Estructura:** El código usa un `while` principal para ir pidiendo los tanqueos y un `while` anidado adentro para validar el octanaje.
* **Decimales:** Todos los resultados finales salen formateados con exactamente 2 decimales.

## 🚀 Cómo correr el programa

Para ejecutar el script desde la terminal de tu entorno de desarrollo, corre el siguiente comando:
```bash
python Taller_estructuras_de_control_iterativas.py