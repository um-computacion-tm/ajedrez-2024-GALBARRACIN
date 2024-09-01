## Ajedrez con Modulo Pygame 

 Este proyecto se basa en un ajedrez por turnos para dos personas, usando el módulo de PyGame. Cada vez que un jugador pierda una pieza esta aparecerá del lado derecho de la pantalla.

 ## Tests Unitarios

Este proyecto incluye una suite de tests unitarios que aseguran que las funciones principales relacionadas con el movimiento de piezas en el ajedrez funcionen correctamente.

### Cómo ejecutar las pruebas

Guarda el archivo de prueba como test.py en el mismo directorio que main.py.

Ejecuta las pruebas utilizando Python:

" python -m unittest test.py "

### ¿Cómo funcionan los tests?

1. *Configuración inicial*: Cada test configura las condiciones necesarias para ejecutar la función que se va a probar. Esto puede incluir la posición de las piezas en el tablero de ajedrez y cualquier otro estado relevante.

2. *Ejecución de la función*: El test llama a la función objetivo con los parámetros configurados en el paso anterior.

3. *Verificación de resultados (Assertions): Los tests verifican que el resultado devuelto por la función coincida con el resultado esperado utilizando **assertions*. Por ejemplo, se podría usar assertEqual() para comparar el resultado real con el esperado.

4. *Resultados del test*: Si todas las condiciones del test se cumplen, el test pasa. Si alguna verificación falla, el test no pasa, indicando un posible problema en la función probada.