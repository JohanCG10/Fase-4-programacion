from servicio import Servicio
from excepciones import (
    ServicioInvalidoError,
    ServicioNoDisponibleError
)


# Clase para representar el servicio de asesoría especializada.
class AsesoriaEspecializada(Servicio):

    def __init__(
        self,
        id_servicio,
        nombre,
        tarifa,
        disponible,
        area_especialidad,
        duracion
    ):

        # Se ejecuta el constructor de la clase Servicio.
        super().__init__(
            id_servicio,
            nombre,
            tarifa,
            disponible
        )

        # Se guardan los datos propios de la asesoría.
        self._area_especialidad = area_especialidad
        self._duracion = duracion

        # Se validan los datos propios de la asesoría.
        self.validar_parametros()

    # Verifica que los datos de la asesoría sean válidos.
    def validar_parametros(self):

        if self._area_especialidad == "":
            raise ServicioInvalidoError(
                "El área de especialidad no puede estar vacía."
            )

        if self._duracion <= 0:
            raise ServicioInvalidoError(
                "La duración de la asesoría debe ser mayor que cero."
            )

        return True

    # Calcula el costo de la asesoría con impuesto y descuento opcionales.
    def calcular_costo(self, impuesto=0, descuento=0):

        if self._disponible == False:
            raise ServicioNoDisponibleError(
                "La asesoría no se encuentra disponible."
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

    # Devuelve una descripción de la asesoría.
    def describir(self):

        descripcion = (
            f"Servicio: {self._nombre}\n"
            f"Área de especialidad: {self._area_especialidad}\n"
            f"Duración: {self._duracion} horas\n"
            f"Tarifa por hora: ${self._tarifa}"
        )

        return descripcion

    # Devuelve el área de especialidad.
    def obtener_area_especialidad(self):

        return self._area_especialidad

    # Devuelve la duración de la asesoría.
    def obtener_duracion(self):

        return self._duracion