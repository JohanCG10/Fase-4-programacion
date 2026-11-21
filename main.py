from cliente import Cliente
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada
from reserva import Reserva
from sistema import Sistema

from excepciones import (
    ClienteInvalidoError,
    ServicioInvalidoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    OperacionNoPermitidaError
)

from logger_config import logger


# Se crea el objeto principal del sistema.
sistema = Sistema()


print("===================================")
print("SISTEMA DE RESERVAS - SOFTWARE FJ")
print("===================================")


# =========================================================
# OPERACIÓN 1: REGISTRAR UN CLIENTE VÁLIDO
# =========================================================

print("\nOPERACIÓN 1: Registrar cliente válido")

try:

    cliente_1 = Cliente(
        "1054",
        "Johan García",
        "johan@gmail.com"
    )

    sistema.agregar_cliente(cliente_1)

except ClienteInvalidoError as error:

    print(f"Error: {error}")

    logger.error(
        f"Error al registrar cliente: {error}"
    )

else:

    print("Cliente registrado correctamente.")
    print(f"Nombre: {cliente_1.obtener_nombre()}")

finally:

    print("Finalizó la operación 1.")


# =========================================================
# OPERACIÓN 2: REGISTRAR UN CLIENTE INVÁLIDO
# =========================================================

print("\nOPERACIÓN 2: Registrar cliente inválido")

try:

    try:

        cliente_invalido = Cliente(
            "2020",
            "Cliente de prueba",
            "correoincorrecto.com"
        )

        sistema.agregar_cliente(
            cliente_invalido
        )

    except ClienteInvalidoError as error_original:

        # Se crea una nueva excepción conservando
        # la causa del error original.
        raise ClienteInvalidoError(
            "No fue posible registrar el cliente."
        ) from error_original

except ClienteInvalidoError as error:

    print(f"Error controlado: {error}")
    print(f"Causa original: {error.__cause__}")

    logger.exception(
        "Se intentó registrar un cliente inválido."
    )

finally:

    print("El programa continúa funcionando.")


# =========================================================
# OPERACIÓN 3: REGISTRAR UN CLIENTE REPETIDO
# =========================================================

print("\nOPERACIÓN 3: Registrar cliente repetido")

try:

    cliente_repetido = Cliente(
        "1054",
        "Otro cliente",
        "otro@gmail.com"
    )

    sistema.agregar_cliente(
        cliente_repetido
    )

except ClienteInvalidoError as error:

    print(f"Error controlado: {error}")

    logger.warning(
        f"Cliente repetido detectado: {error}"
    )

finally:

    print("Finalizó la operación 3.")


# =========================================================
# OPERACIÓN 4: REGISTRAR LOS TRES SERVICIOS
# =========================================================

print("\nOPERACIÓN 4: Registrar los servicios")

try:

    sala_1 = ReservaSala(
        "S001",
        "Sala de reuniones",
        25000,
        True,
        12,
        3
    )

    equipo_1 = AlquilerEquipo(
        "E001",
        "Alquiler de computadores",
        15000,
        False,
        "Computador portátil",
        2,
        4
    )

    asesoria_1 = AsesoriaEspecializada(
        "A001",
        "Asesoría de programación",
        50000,
        True,
        "Programación en Python",
        2
    )

    sistema.agregar_servicio(sala_1)
    sistema.agregar_servicio(equipo_1)
    sistema.agregar_servicio(asesoria_1)

except ServicioInvalidoError as error:

    print(f"Error: {error}")

    logger.error(
        f"Error al registrar servicio: {error}"
    )

else:

    print("Los servicios fueron registrados.")

    # Se demuestra el polimorfismo.
    # Todos son servicios, pero cada objeto
    # ejecuta su propia versión de describir().
    lista_servicios = (
        sistema.obtener_servicios()
    )

    for servicio in lista_servicios:

        print("\n----------------------------")
        print(servicio.describir())

finally:

    print("Finalizó la operación 4.")


# =========================================================
# OPERACIÓN 5: CREAR UNA RESERVA DE SALA
# =========================================================

print("\nOPERACIÓN 5: Crear reserva de sala")

try:

    reserva_1 = Reserva(
        "R001",
        cliente_1,
        sala_1
    )

    sistema.agregar_reserva(
        reserva_1
    )

except ReservaInvalidaError as error:

    print(f"Error: {error}")

    logger.error(
        f"Error al crear reserva: {error}"
    )

else:

    print("Reserva creada correctamente.")
    print(reserva_1.mostrar_informacion())

finally:

    print("Finalizó la operación 5.")


# =========================================================
# OPERACIÓN 6: CONFIRMAR LA RESERVA
# =========================================================

print("\nOPERACIÓN 6: Confirmar reserva")

try:

    mensaje = reserva_1.confirmar()

except (
    OperacionNoPermitidaError,
    ServicioNoDisponibleError
) as error:

    print(f"Error: {error}")

    logger.error(
        f"No fue posible confirmar la reserva: {error}"
    )

else:

    print(mensaje)

    logger.info(
        "La reserva R001 fue confirmada."
    )

finally:

    print("Finalizó la operación 6.")


# =========================================================
# OPERACIÓN 7: PROCESAR LA RESERVA
# =========================================================

print("\nOPERACIÓN 7: Procesar reserva")

try:

    costo_reserva = reserva_1.procesar()

except (
    OperacionNoPermitidaError,
    ServicioNoDisponibleError,
    ServicioInvalidoError
) as error:

    print(f"Error: {error}")

    logger.error(
        f"No fue posible procesar la reserva: {error}"
    )

else:

    print("Reserva procesada correctamente.")
    print(f"Costo total: ${costo_reserva}")

    logger.info(
        f"Reserva R001 procesada. "
        f"Costo: ${costo_reserva}"
    )

finally:

    print("Finalizó la operación 7.")


# =========================================================
# OPERACIÓN 8: USAR UN SERVICIO NO DISPONIBLE
# =========================================================

print(
    "\nOPERACIÓN 8: Reserva con servicio no disponible"
)

try:

    reserva_2 = Reserva(
        "R002",
        cliente_1,
        equipo_1
    )

    sistema.agregar_reserva(
        reserva_2
    )

    reserva_2.confirmar()

except ServicioNoDisponibleError as error:

    print(f"Error controlado: {error}")

    logger.warning(
        f"Servicio no disponible: {error}"
    )

except ReservaInvalidaError as error:

    print(f"Error en la reserva: {error}")

    logger.error(
        f"Reserva inválida: {error}"
    )

finally:

    print(
        "La aplicación continúa después del error."
    )


# =========================================================
# OPERACIÓN 9: SOBRECARGA SIMULADA DEL CÁLCULO
# =========================================================

print("\nOPERACIÓN 9: Calcular costos opcionales")

try:

    # Forma 1: cálculo básico.
    costo_basico = (
        asesoria_1.calcular_costo()
    )

    # Forma 2: cálculo con impuesto.
    costo_con_impuesto = (
        asesoria_1.calcular_costo(19)
    )

    # Forma 3: impuesto y descuento.
    costo_con_descuento = (
        asesoria_1.calcular_costo(
            19,
            10
        )
    )

except (
    ServicioInvalidoError,
    ServicioNoDisponibleError
) as error:

    print(f"Error: {error}")

    logger.error(
        f"Error en el cálculo: {error}"
    )

else:

    print(f"Costo básico: ${costo_basico}")

    print(
        f"Costo con impuesto: "
        f"${costo_con_impuesto}"
    )

    print(
        f"Costo con impuesto y descuento: "
        f"${costo_con_descuento}"
    )

    logger.info(
        "Se realizaron cálculos con parámetros opcionales."
    )

finally:

    print("Finalizó la operación 9.")


# =========================================================
# OPERACIÓN 10: CANCELAR UNA RESERVA PROCESADA
# =========================================================

print(
    "\nOPERACIÓN 10: Cancelar reserva procesada"
)

try:

    mensaje = reserva_1.cancelar()

except OperacionNoPermitidaError as error:

    print(f"Error controlado: {error}")

    logger.warning(
        f"Operación no permitida: {error}"
    )

else:

    print(mensaje)

finally:

    print("Finalizó la operación 10.")
    print("El sistema sigue funcionando.")


# =========================================================
# RESUMEN FINAL
# =========================================================

print("\n===================================")
print("RESUMEN DEL SISTEMA")
print("===================================")

print(
    f"Clientes registrados: "
    f"{len(sistema.obtener_clientes())}"
)

print(
    f"Servicios registrados: "
    f"{len(sistema.obtener_servicios())}"
)

print(
    f"Reservas registradas: "
    f"{len(sistema.obtener_reservas())}"
)

print("\nLa simulación terminó correctamente.")

logger.info(
    "La simulación de las diez operaciones terminó."
)