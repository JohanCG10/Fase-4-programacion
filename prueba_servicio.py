from servicio import Servicio
from excepciones import ServicioInvalidoError


class ServicioPrueba(Servicio):

    def calcular_costo(self):
        return self._tarifa

    def describir(self):
        return self._nombre

    def validar_parametros(self):
        return True


try:
    servicio = ServicioPrueba("S01", "Reserva de sala", 50000, True)

    print("Servicio creado correctamente")
    print("Nombre:", servicio.obtener_nombre())
    print("Tarifa:", servicio.obtener_tarifa())
    print("Disponible:", servicio.obtener_disponibilidad())

    servicio_invalido = ServicioPrueba("S02", "Sala", -100, True)

except ServicioInvalidoError as error:
    print("Validación correcta:", error)
