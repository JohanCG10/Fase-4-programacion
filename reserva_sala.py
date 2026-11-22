from servicio import Servicio
from excepciones import ServicioInvalidoError, ServicioNoDisponibleError


# Clase que representa el servicio de reserva de salas.
class ReservaSala(Servicio):

    def __init__(self, id_servicio, nombre, tarifa,
                 disponible, capacidad, duracion):

        # Utilizamos los datos de la clase Servicio.
        super().__init__(id_servicio, nombre, tarifa, disponible)

        self._capacidad = capacidad
        self._duracion = duracion

        # Validamos los datos de la reserva.
        self.validar_parametros()

    # Comprueba la capacidad y duración de la sala.
    def validar_parametros(self):

        if type(self._capacidad) != int:
            raise ServicioInvalidoError(
                "La capacidad debe ser un número entero."
            )

        if self._capacidad <= 0:
            raise ServicioInvalidoError(
                "La capacidad de la sala debe ser mayor que cero."
            )

        if isinstance(self._duracion, bool) or not isinstance(
            self._duracion, (int, float)
        ):
            raise ServicioInvalidoError(
                "La duración debe ser un número."
            )

        if self._duracion <= 0:
            raise ServicioInvalidoError(
                "La duración debe ser mayor que cero."
            )

        return True

    # Calcula el costo de la reserva.
    def calcular_costo(self, impuesto=0, descuento=0):

        if not self._disponible:
            raise ServicioNoDisponibleError(
                "La sala no se encuentra disponible."
            )

        if isinstance(impuesto, bool) or not isinstance(
            impuesto, (int, float)
        ):
            raise ServicioInvalidoError(
                "El impuesto debe ser un número."
            )

        if isinstance(descuento, bool) or not isinstance(
            descuento, (int, float)
        ):
            raise ServicioInvalidoError(
                "El descuento debe ser un número."
            )

        if impuesto < 0:
            raise ServicioInvalidoError(
                "El impuesto no puede ser negativo."
            )

        if descuento < 0 or descuento > 100:
            raise ServicioInvalidoError(
                "El descuento debe estar entre 0 y 100."
            )

        costo_base = self._tarifa * self._duracion
        valor_impuesto = costo_base * impuesto / 100
        valor_descuento = costo_base * descuento / 100

        costo_total = costo_base + valor_impuesto - valor_descuento

        return costo_total

    # Muestra la información de la reserva.
    def describir(self):

        descripcion = (
            f"Servicio: {self._nombre}\n"
            f"Capacidad: {self._capacidad} personas\n"
            f"Duración: {self._duracion} horas\n"
            f"Tarifa por hora: ${self._tarifa}"
        )

        return descripcion

    # Métodos para consultar los datos de la sala.
    def obtener_capacidad(self):
        return self._capacidad

    def obtener_duracion(self):
        return self._duracion