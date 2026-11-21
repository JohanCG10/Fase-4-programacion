from servicio import Servicio
from excepciones import (
    ServicioInvalidoError,
    ServicioNoDisponibleError
)


# Clase para representar el servicio de reserva de una sala.
class ReservaSala(Servicio):

    def __init__(
        self,
        id_servicio,
        nombre,
        tarifa,
        disponible,
        capacidad,
        duracion
    ):

        # Se ejecuta el constructor de la clase Servicio.
        super().__init__(
            id_servicio,
            nombre,
            tarifa,
            disponible
        )

        # Se guardan los datos propios de la sala.
        self._capacidad = capacidad
        self._duracion = duracion

        # Se validan los datos propios de la sala.
        self.validar_parametros()

    # Verifica que la capacidad y la duración sean válidas.
    def validar_parametros(self):

        if self._capacidad <= 0:
            raise ServicioInvalidoError(
                "La capacidad de la sala debe ser mayor que cero."
            )

        if self._duracion <= 0:
            raise ServicioInvalidoError(
                "La duración de la reserva debe ser mayor que cero."
            )

        return True

    # Calcula el costo con impuesto y descuento opcionales.
    def calcular_costo(
        self,
        impuesto=0,
        descuento=0
    ):

        if self._disponible == False:
            raise ServicioNoDisponibleError(
                "La sala no se encuentra disponible."
            )

        if impuesto < 0:
            raise ServicioInvalidoError(
                "El impuesto no puede ser negativo."
            )

        if descuento < 0:
            raise ServicioInvalidoError(
                "El descuento no puede ser negativo."
            )

        costo_base = (
            self._tarifa * self._duracion
        )

        valor_impuesto = (
            costo_base * impuesto / 100
        )

        valor_descuento = (
            costo_base * descuento / 100
        )

        costo_total = (
            costo_base
            + valor_impuesto
            - valor_descuento
        )

        return costo_total

    # Devuelve una descripción de la reserva de sala.
    def describir(self):

        descripcion = (
            f"Servicio: {self._nombre}\n"
            f"Capacidad: {self._capacidad} personas\n"
            f"Duración: {self._duracion} horas\n"
            f"Tarifa por hora: ${self._tarifa}"
        )

        return descripcion

    # Devuelve la capacidad de la sala.
    def obtener_capacidad(self):

        return self._capacidad

    # Devuelve la duración de la reserva.
    def obtener_duracion(self):

        return self._duracion