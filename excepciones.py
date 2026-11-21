# Excepción para los errores relacionados con clientes.
class ClienteInvalidoError(Exception):
    pass


# Excepción para errores relacionados con los servicios.
class ServicioInvalidoError(Exception):
    pass


# Excepción para servicios que no se encuentran disponibles.
class ServicioNoDisponibleError(Exception):
    pass


# Excepción para errores relacionados con las reservas.
class ReservaInvalidaError(Exception):
    pass


# Excepción para acciones que no se pueden realizar.
class OperacionNoPermitidaError(Exception):
    pass