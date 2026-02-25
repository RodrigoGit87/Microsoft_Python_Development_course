# Extraer: lea de forma inteligente los datos relevantes de cada archivo, filtrando el ruido y la información irrelevante.
# Python proporciona bibliotecas como pandas, que simplifican el proceso de lectura de datos de diversos formatos 
# de archivo (por ejemplo, CSV o Excel) y su manipulación de forma estructurada. Puede seleccionar fácilmente columnas 
# específicas, filtrar filas basándose en condiciones y extraer los datos que necesita para su análisis.
# Ejemplo:
import csv
#AUTOMATIZACION BÁSICA
# Read a CSV file
#Esto hace dos cosas a la vez:
# 1. open('data.csv', mode='r') — Abre el archivo data.csv
# 'data.csv' → el nombre/ruta del archivo
# mode='r' → modo read (lectura). Solo lee, no modifica el archivo.
# Otros modos comunes: 'w' (escribir/sobrescribir), 'a' (añadir al final)

#for row in csv_reader: 
# Es un bucle for que recorre cada elemento de csv_reader uno por uno:
# csv_reader contiene todas las filas del CSV
# En cada vuelta del bucle, row toma el valor de una fila (como una lista)
# print(row) imprime esa fila
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)


#AUTOMATIZACION AVANZADA
# Transformación: Esta etapa implica el uso de métodos estadísticos y algoritmos para descubrir patrones ocultos en 
# sus datos. Las bibliotecas de Python como NumPy, SciPy y Scikit-learn proporcionan las herramientas para ello.

# Visualizar:  Aquí crearás gráficos y diagramas para que tus datos sean claros y comprensibles.
# Bibliotecas como Matplotlib y Apache Superset te ayudarán a hacerlo.

# Informe: Por último, resumirás tus conclusiones en un informe claro, destacando los puntos clave. 
# Las funciones de procesamiento de texto de Python y herramientas como Jupyter Notebooks lo hacen posible. 
# 
# Web scraping: Extracción automática de datos de sitios web, 
# como precios de productos, artículos de noticias o posts en redes sociales.
# 
# Automatización del correo electrónico: Envío de correos electrónicos personalizados a un gran número de destinatarios, 
# programación de recordatorios o filtrado de correos electrónicos entrantes en función de criterios específicos.
#
#Automatización de pruebas: Escritura de secuencias de comandos para automatizar las pruebas de aplicaciones de software,
# garantizando que funcionen correctamente en diversas condiciones.         

