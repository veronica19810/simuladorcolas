from utils.funciones import simular_cola, mostrar_resultados

def main():
    print("🎯 SIMULADOR DE SISTEMA DE COLAS 🎯")
    print("-----------------------------------")

    llegada = float(input("👉 Ingrese la tasa de llegada (ejemplo 0.5): "))
    servicio = float(input("👉 Ingrese la tasa de servicio (ejemplo 0.8): "))
    clientes = int(input("👉 Ingrese el número de clientes a simular: "))

    resultados = simular_cola(llegada, servicio, clientes)
    mostrar_resultados(resultados, llegada, servicio)

if __name__ == "__main__":
    main()
