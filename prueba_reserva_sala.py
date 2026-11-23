
from reserva_sala import ReservaSala
from excepciones import ServicioInvalidoError, ServicioNoDisponibleError

# Prueba de una reserva correcta
try:
    sala = ReservaSala("S01", "Sala de reuniones", 50000, True, 10, 3)

    print("RESERVA DE SALA")
    print(sala.describir())
    print("Costo total:", sala.calcular_costo())
    print("Costo con impuesto:", sala.calcular_costo(impuesto=19))
    print("Costo con descuento:", sala.calcular_costo(descuento=10))

except (ServicioInvalidoError, ServicioNoDisponibleError) as error:
    print("Error:", error)


# Prueba con capacidad incorrecta
try:
    sala_invalida = ReservaSala("S02", "Sala pequeña", 30000, True, -5, 2)

except ServicioInvalidoError as error:
    print("Validación correcta:", error)


# Prueba con sala no disponible
try:
    sala_ocupada = ReservaSala("S03", "Sala ocupada", 40000, False, 8, 2)
    sala_ocupada.calcular_costo()

except ServicioNoDisponibleError as error:
    print("Disponibilidad correcta:", error)