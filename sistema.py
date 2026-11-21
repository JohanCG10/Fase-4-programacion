from excepciones import (
    ClienteInvalidoError,
    ServicioInvalidoError,
    ReservaInvalidaError
)

from logger_config import logger


# Clase encargada de gestionar los datos principales del sistema.
class Sistema:

    def __init__(self):

        # Listas internas para guardar los objetos.
        self._clientes = []
        self._servicios = []
        self._reservas = []

    # Agrega un cliente a la lista.
    def agregar_cliente(self, cliente):

        identificacion = (
            cliente.obtener_identificacion()
        )

        cliente_encontrado = (
            self.buscar_cliente(identificacion)
        )

        if cliente_encontrado is not None:

            logger.warning(
                f"Intento de registrar un cliente repetido: "
                f"{identificacion}"
            )

            raise ClienteInvalidoError(
                "Ya existe un cliente con esa identificación."
            )

        self._clientes.append(cliente)

        logger.info(
            f"Cliente registrado correctamente: "
            f"{identificacion}"
        )

        return True

    # Busca un cliente mediante su identificación.
    def buscar_cliente(self, identificacion):

        cliente_encontrado = None

        for cliente in self._clientes:

            if (
                cliente.obtener_identificacion()
                == identificacion
            ):

                cliente_encontrado = cliente
                break

        return cliente_encontrado

    # Agrega un servicio a la lista.
    def agregar_servicio(self, servicio):

        id_servicio = (
            servicio.obtener_id_servicio()
        )

        servicio_encontrado = (
            self.buscar_servicio(id_servicio)
        )

        if servicio_encontrado is not None:

            logger.warning(
                f"Intento de registrar un servicio repetido: "
                f"{id_servicio}"
            )

            raise ServicioInvalidoError(
                "Ya existe un servicio con ese identificador."
            )

        self._servicios.append(servicio)

        logger.info(
            f"Servicio registrado correctamente: "
            f"{id_servicio}"
        )

        return True

    # Busca un servicio mediante su identificador.
    def buscar_servicio(self, id_servicio):

        servicio_encontrado = None

        for servicio in self._servicios:

            if (
                servicio.obtener_id_servicio()
                == id_servicio
            ):

                servicio_encontrado = servicio
                break

        return servicio_encontrado

    # Agrega una reserva a la lista.
    def agregar_reserva(self, reserva):

        id_reserva = (
            reserva.obtener_id_reserva()
        )

        reserva_encontrada = (
            self.buscar_reserva(id_reserva)
        )

        if reserva_encontrada is not None:

            logger.warning(
                f"Intento de registrar una reserva repetida: "
                f"{id_reserva}"
            )

            raise ReservaInvalidaError(
                "Ya existe una reserva con ese identificador."
            )

        self._reservas.append(reserva)

        logger.info(
            f"Reserva registrada correctamente: "
            f"{id_reserva}"
        )

        return True

    # Busca una reserva mediante su identificador.
    def buscar_reserva(self, id_reserva):

        reserva_encontrada = None

        for reserva in self._reservas:

            if (
                reserva.obtener_id_reserva()
                == id_reserva
            ):

                reserva_encontrada = reserva
                break

        return reserva_encontrada

    # Devuelve la lista de clientes registrados.
    def obtener_clientes(self):

        return self._clientes

    # Devuelve la lista de servicios registrados.
    def obtener_servicios(self):

        return self._servicios

    # Devuelve la lista de reservas registradas.
    def obtener_reservas(self):

        return self._reservas