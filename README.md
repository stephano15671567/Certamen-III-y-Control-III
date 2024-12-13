Proyecto de Búsqueda con Índice Invertido

Descripción General

Este proyecto implementa un sistema de búsqueda basado en un índice invertido, procesando un conjunto de documentos y permitiendo realizar consultas eficientemente. El sistema elimina palabras irrelevantes (stopwords) y soporta consultas complejas mediante intersección recursiva de términos. 

Archivos Principales

build_index.awk: Genera un índice invertido a partir de un conjunto de documentos (gov2_pages.dat).

clean_words.py: Limpia el índice invertido eliminando palabras irrelevantes (stopwords) y genera un archivo limpio (clean_index.txt).

custom_search.py: Realiza búsquedas en el índice invertido procesado. Soporta consultas ingresadas por teclado y aplica intersección recursiva para encontrar resultados.

custom_index.txt: Archivo generado que contiene el índice invertido limpio.

gov2_pages.dat: Archivo fuente de documentos con datos en formato delimitado.

query_list.txt: Lista de consultas a ser procesadas (opcional si las consultas se ingresan por teclado).

query_output.txt: Archivo de salida que contiene los resultados de las consultas.

filter_log.txt: Registro de palabras eliminadas durante el proceso de limpieza.

Configuración y Ejecución

1. Generar el índice invertido

Ejecuta el script build_index.awk para generar un índice invertido inicial:

awk -f build_index.awk gov2_pages.dat

Esto generará un archivo intermedio (new_inverted_index.txt) que contiene el índice invertido preliminar.

2. Limpiar el índice invertido

Ejecuta el script clean_words.py para eliminar palabras irrelevantes (stopwords):

python clean_words.py

Salida:

clean_index.txt: Contiene el índice invertido limpio.

filter_log.txt: Lista de palabras eliminadas.

3. Realizar búsquedas

Ejecuta el script custom_search.py para realizar consultas:

python custom_search.py

Este script permite ingresar consultas por teclado. Cada término de la consulta debe estar separado por espacios. Para salir, escribe salir.

Ejemplo de Uso:

Ingrese la consulta (o 'salir' para terminar): nasa research
Resultados encontrados para 'nasa research':
http://example1.gov, http://example2.gov

Ingrese la consulta (o 'salir' para terminar): internet science
Resultados encontrados para 'internet science':
http://example3.gov

Ingrese la consulta (o 'salir' para terminar): salir
Saliendo del buscador.

Opcional: Procesar una lista de consultas

Si deseas usar una lista predefinida de consultas (almacenada en query_list.txt), modifica el script custom_search.py para que lea de ese archivo y guarde los resultados en query_output.txt.