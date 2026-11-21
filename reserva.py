from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ServicioNoDisponibleError
)


# Clase que relaciona un cliente con un servicio.
class Reserva:

    def __init__(
        self,
        id_reserva,
        cliente,
        servicio
    ):

        # Se validan los datos antes de guardarlos.
        if id_reserva == "":
            raise ReservaInvalidaError(
                "El identificador de la reserva no puede estar vacío."
            )

        if cliente is None:
            raise ReservaInvalidaError(
                "La reserva debe tener un cliente."
            )

        if servicio is None:
            raise ReservaInvalidaError(
                "La reserva debe tener un servicio."
            )

        # Se guardan los datos de la reserva.
        self._id_reserva = id_reserva
        self._cliente = cliente
        self._servicio = servicio

        # Todas las reservas comienzan pendientes.
        self._estado = "Pendiente"

        # Al comienzo todavía no existe un costo calculado.
        self._costo_total = 0

    # Confirma una reserva que se encuentra pendiente.
    def confirmar(self):

        if self._estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        if self._servicio.obtener_disponibilidad() == False:
            raise ServicioNoDisponibleError(
                "El servicio no se encuentra disponible."
            )

        self._estado = "Confirmada"

        return (
            f"La reserva {self._id_reserva} "
            f"fue confirmada correctamente."
        )

    # Cancela una reserva pendiente o confirmada.
    def cancelar(self):

        if self._estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        if self._estado == "Procesada":
            raise OperacionNoPermitidaError(
                "Una reserva procesada no se puede cancelar."
            )

        self._estado = "Cancelada"

        return (
            f"La reserva {self._id_reserva} "
            f"fue cancelada correctamente."
        )

    # Procesa una reserva que ya fue confirmada.
    def procesar(self):

        if self._estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "Solo se pueden procesar reservas confirmadas."
            )

        # Se calcula el costo utilizando el servicio correspondiente.
        self._costo_total = (
            self._servicio.calcular_costo()
        )

        self._estado = "Procesada"

        return self._costo_total

    # Muestra la información principal de la reserva.
    def mostrar_informacion(self):

        informacion = (
            f"Reserva: {self._id_reserva}\n"
            f"Cliente: {self._cliente.obtener_nombre()}\n"
            f"Servicio: {self._servicio.obtener_nombre()}\n"
            f"Estado: {self._estado}\n"
            f"Costo total: ${self._costo_total}"
        )

        return informacion

    # Devuelve el identificador de la reserva.
    def obtener_id_reserva(self):

        return self._id_reserva

    # Devuelve el cliente relacionado con la reserva.
    def obtener_cliente(self):

        return self._cliente

    # Devuelve el servicio relacionado con la reserva.
    def obtener_servicio(self):

        return self._servicio

    # Devuelve el estado actual de la reserva.
    def obtener_estado(self):

        return self._estado

    # Devuelve el costo total de la reserva.
    def obtener_costo_total(self):

        return self._costo_total