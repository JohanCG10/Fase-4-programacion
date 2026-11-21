from servicio import Servicio
from excepciones import (
    ServicioInvalidoError,
    ServicioNoDisponibleError
)


# Clase para representar el servicio de alquiler de equipos.
class AlquilerEquipo(Servicio):

    def __init__(
        self,
        id_servicio,
        nombre,
        tarifa,
        disponible,
        nombre_equipo,
        cantidad,
        duracion
    ):

        # Se ejecuta el constructor de la clase Servicio.
        super().__init__(
            id_servicio,
            nombre,
            tarifa,
            disponible
        )

        # Se guardan los datos propios del alquiler.
        self._nombre_equipo = nombre_equipo
        self._cantidad = cantidad
        self._duracion = duracion

        # Se validan los datos propios del alquiler.
        self.validar_parametros()

    # Verifica que los datos del alquiler sean válidos.
    def validar_parametros(self):

        if self._nombre_equipo == "":
            raise ServicioInvalidoError(
                "El nombre del equipo no puede estar vacío."
            )

        if self._cantidad <= 0:
            raise ServicioInvalidoError(
                "La cantidad de equipos debe ser mayor que cero."
            )

        if self._duracion <= 0:
            raise ServicioInvalidoError(
                "La duración del alquiler debe ser mayor que cero."
            )

        return True

    # Calcula el costo del alquiler con impuesto y descuento opcionales.
    def calcular_costo(self, impuesto=0, descuento=0):

        if self._disponible == False:
            raise ServicioNoDisponibleError(
                "El equipo no se encuentra disponible."
            )

        if impuesto < 0:
            raise ServicioInvalidoError(
                "El impuesto no puede ser negativo."
            )

        if descuento < 0:
            raise ServicioInvalidoError(
                "El descuento no puede ser negativo."
            )

        costo_por_equipo = (
            self._tarifa * self._duracion
        )

        costo_base = (
            costo_por_equipo * self._cantidad
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
    
    # Devuelve una descripción del alquiler.
    def describir(self):

        descripcion = (
            f"Servicio: {self._nombre}\n"
            f"Equipo: {self._nombre_equipo}\n"
            f"Cantidad: {self._cantidad}\n"
            f"Duración: {self._duracion} horas\n"
            f"Tarifa por equipo y hora: ${self._tarifa}"
        )

        return descripcion

    # Devuelve el nombre del equipo.
    def obtener_nombre_equipo(self):

        return self._nombre_equipo

    # Devuelve la cantidad de equipos.
    def obtener_cantidad(self):

        return self._cantidad

    # Devuelve la duración del alquiler.
    def obtener_duracion(self):

        return self._duracion