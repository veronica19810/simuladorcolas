import random
import csv

def simular_cola(llegada, servicio, clientes):
    tiempo_actual = 0
    tiempo_salida = 0
    resultados = []

    for i in range(clientes):
        tiempo_llegada = random.expovariate(llegada)
        tiempo_actual += tiempo_llegada
        tiempo_servicio = random.expovariate(servicio)

        if tiempo_actual < tiempo_salida:
            espera = tiempo_salida - tiempo_actual
        else:
            espera = 0

        tiempo_salida = tiempo_actual + espera + tiempo_servicio
        tiempo_total = espera + tiempo_servicio

        resultados.append([
            i + 1,
            round(tiempo_actual, 2),
            round(espera, 2),
            round(tiempo_servicio, 2),
            round(tiempo_total, 2)
        ])

    return resultados

def mostrar_resultados(resultados, llegada, servicio):
    clientes = len(resultados)
    total_espera = sum([r[2] for r in resultados]) / clientes
    total_sistema = sum([r[4] for r in resultados]) / clientes
    utilizacion = llegada / servicio

    print("\n RESULTADOS DEL SIMULADOR:")
    print(f"Promedio de espera: {total_espera:.2f} minutos")
    print(f"Promedio total en el sistema: {total_sistema:.2f} minutos")
    print(f"Utilización del sistema: {utilizacion:.2f}")

    with open('data/resultados.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Cliente", "Llegada", "Espera", "Servicio", "Total"])
        writer.writerows(resultados)

    print("\n Resultados guardados en 'data/resultados.csv'")
