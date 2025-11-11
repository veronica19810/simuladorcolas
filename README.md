# SIMULADOR DE SISTEMA DE COLAS
Este es un proyecto de consola hecho en Python que simula un sistema de colas (por ejemplo, una fila en un supermercado), donde los clientes llegan, esperan y son atendidos de manera aleatoria.
El programa calcula métricas como tiempos de espera, atención y utilización del sistema, además de guardar los resultados en un archivo CSV.

# ¿QUÉ HACE ESTE PROGRAMA?
	•	Simula llegadas y servicios aleatorios usando distribución exponencial.
	•	Calcula el tiempo promedio de espera y de servicio.g
	•	Guarda los datos de la simulación en un archivo CSV para análisis posterior.

# ¿CÓMO EJECUTAR EL PROYECTO?
	1.	Asegúrate de tener Python 3.7 o superior instalado en tu equipo.
	2.	Clona o descarga este repositorio en tu computador.
	3.	Abre una terminal y navega hasta la raíz del proyecto.
	4.	Ejecuta el siguiente comando: python src/main.py 
    5.	Ingresa los valores solicitados en consola:
	•	Tasa de llegada (por ejemplo: 0.5)
	•	Tasa de servicio (por ejemplo: 0.8)
	•	Número de clientes a simular
	6.	Los resultados se mostrarán en pantalla y se guardarán en data/resultados.csv.

# REQUISITOS
Este proyecto no requiere librerías externas.
Solo usa módulos estándar de Python como:
	•	random → genera tiempos aleatorios de llegada y servicio para simular el comportamiento real de una cola.
	•	csv → guarda los resultados de la simulación en un archivo CSV para analizarlos fácilmente.

# AUTORES
Autores
	•	DARA JULIETH POLO DUMAR
	•	VERÓNICA RESTÁN DOVAL 
	•	ISABELLA FRANCO PATIÑO
    
Este proyecto fue desarrollado con fines académicos y puede ser reutilizado para el aprendizaje de simulación de colas y estructuras computacionales.
