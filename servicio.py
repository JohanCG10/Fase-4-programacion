from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError


# Clase abstracta que contiene los datos comunes de los servicios.
class Servicio(ABC):

    def __init__(self, id_servicio, nombre, tarifa, disponible):

        # Primero se validan los datos recibidos.
        self.validar_datos(
            id_servicio,
            nombre,
            tarifa
        )

        # Después se guardan los datos del servicio.
        self._id_servicio = id_servicio
        self._nombre = nombre
        self._tarifa = tarifa
        self._disponible = disponible

    # Verifica que los datos básicos del servicio sean válidos.
    def validar_datos(
        self,
        id_servicio,
        nombre,
        tarifa
    ):

        if id_servicio == "":
            raise ServicioInvalidoError(
                "El identificador del servicio no puede estar vacío."
            )

        if nombre == "":
            raise ServicioInvalidoError(
                "El nombre del servicio no puede estar vacío."
            )

        if tarifa <= 0:
            raise ServicioInvalidoError(
                "La tarifa debe ser mayor que cero."
            )

        return True

    # Método que cada servicio utilizará para calcular su costo.
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método que cada servicio utilizará para mostrar su información.
    @abstractmethod
    def describir(self):
        pass

    # Método que cada servicio utilizará para validar sus datos propios.
    @abstractmethod
    def validar_parametros(self):
        pass

    # Devuelve el identificador del servicio.
    def obtener_id_servicio(self):
        return self._id_servicio

    # Devuelve el nombre del servicio.
    def obtener_nombre(self):
        return self._nombre

    # Devuelve la tarifa del servicio.
    def obtener_tarifa(self):
        return self._tarifa

    # Devuelve si el servicio está disponible.
    def obtener_disponibilidad(self):
        return self._disponible

    # Permite cambiar la disponibilidad del servicio.
    def cambiar_disponibilidad(self, disponible):
        self._disponible = disponible