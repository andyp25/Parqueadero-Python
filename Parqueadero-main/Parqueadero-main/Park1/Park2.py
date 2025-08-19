parqueadero = []

capacidad_carros = 5
capacidad_motos = 3

tarifa_carro = 2000
tarifa_moto = 1000

def mostrar_menu():
    print("\n--- Parqueadero ---")
    print("1. Ingreso vehículo")
    print("2. Salida vehículo")
    print("3. Listado vehículos en el parqueadero")
    print("4. Salida")

def ingreso_vehiculo():
    if len([v for v in parqueadero if v["tipo"] == "carro"]) >= capacidad_carros:
        print("No hay cupo para carros.")
        return
    if len([v for v in parqueadero if v["tipo"] == "moto"]) >= capacidad_motos:
        print("No hay cupo para motos.")
        return

    placa = input("Ingrese la placa del vehiculo entrante: ").upper()


    for v in parqueadero:
        if v["placa"] == placa:
            print("Este vehículo ya está en el parqueadero.")
            return

    tipo = input("Tipo de vehículo (carro/moto): ").lower()
    if tipo not in ("carro", "moto"):
        print("Ingrese un tipo válido.")
        return

    # Pedir hora de entrada
    hora_entrada = input("Hora de entrada (HH:MM): ")
    if not validar_hora(hora_entrada):
        print("Formato de hora inválido. Debe ser HH:MM")
        return

    vehiculo = {"placa": placa, "tipo": tipo, "hora_entrada": hora_entrada}
    parqueadero.append(vehiculo)
    print("Vehículo ingresó correctamente.")

def retiro_vehiculo():
    placa = input("Ingrese la placa del vehículo saliente: ").upper()
    for i, vehiculo in enumerate(parqueadero):
        if vehiculo["placa"] == placa:
            hora_salida = input("Hora de salida (HH:MM): ")
            if not validar_hora(hora_salida):
                print("Formato de hora inválido. Debe ser HH:MM")
                return

            # Calcular tiempo
            h_e, m_e = map(int, vehiculo["hora_entrada"].split(":"))
            h_s, m_s = map(int, hora_salida.split(":"))
            minutos_entrada = h_e * 60 + m_e
            minutos_salida = h_s * 60 + m_s
            minutos_total = minutos_salida - minutos_entrada
            if minutos_total <= 0:
                minutos_total = 1  # mínimo 1 minuto
            horas = (minutos_total + 59) // 60  # redondear hacia arriba

            # Calcular tarifa
            if vehiculo["tipo"] == "carro":
                total = horas * tarifa_carro
            else:
                total = horas * tarifa_moto

            print(f"Tiempo en parqueadero: {horas} hora(s)")
            print(f"Total a pagar: ${total}")

            parqueadero.pop(i)
            print("Vehículo salió correctamente.")
            return
    print("Vehículo no encontrado.")

def listar_vehiculos():
    if not parqueadero:
        print("No hay vehículos en el parqueadero.")
        return
    print("\nVehículos en el parqueadero:")
    for v in parqueadero:
        print(f"Placa: {v['placa']}, Tipo: {v['tipo']}, Hora entrada: {v['hora_entrada']}")

# Validar formato de hora HH:MM
def validar_hora(hora):
    try:
        h, m = map(int, hora.split(":"))
        return 0 <= h < 24 and 0 <= m < 60
    except:
        return False

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        ingreso_vehiculo()
    elif opcion == "2":
        retiro_vehiculo()
    elif opcion == "3":
        listar_vehiculos()
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida.")
