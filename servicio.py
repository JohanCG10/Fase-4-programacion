
from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError


# Clase abstracta para representar los servicios de la empresa.
class Servicio(ABC):

    def __init__(self, id_servicio, nombre, tarifa, disponible=True):

        # Validamos los datos antes de guardarlos.
        self.validar_datos(id_servicio, nombre, tarifa, disponible)

        self._id_servicio = id_servicio
        self._nombre = nombre
        self._tarifa = tarifa
        self._disponible = disponible

    # Comprueba que los datos generales sean correctos.
    def validar_datos(self, id_servicio, nombre, tarifa, disponible=True):

        if not isinstance(id_servicio, str) or id_servicio.strip() == "":
            raise ServicioInvalidoError(
                "El identificador del servicio no puede estar vacío."
            )

        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ServicioInvalidoError(
                "El nombre del servicio no puede estar vacío."
            )

        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)):
            raise ServicioInvalidoError(
                "La tarifa debe ser un número."
            )

        if tarifa <= 0:
            raise ServicioInvalidoError(
                "La tarifa debe ser mayor que cero."
            )

        if not isinstance(disponible, bool):
            raise ServicioInvalidoError(
                "La disponibilidad debe ser True o False."
            )

        return True

    # Métodos que deben implementar las clases hijas.
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    # Métodos para consultar los atributos.
    def obtener_id_servicio(self):
        return self._id_servicio

    def obtener_nombre(self):
        return self._nombre

    def obtener_tarifa(self):
        return self._tarifa

    def obtener_disponibilidad(self):
        return self._disponible

    # Permite cambiar la disponibilidad del servicio.
    def cambiar_disponibilidad(self, disponible):

        if not isinstance(disponible, bool):
            raise ServicioInvalidoError(
                "La disponibilidad debe ser True o False."
            )

        self._disponible = disponible
