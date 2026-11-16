from excepciones import ClienteInvalidoError

class Cliente:

    def __init__(self, identificacion, nombre, correo):

        # Primero validar los datos
        self.validar_identificacion(identificacion)
        self.validar_nombre(nombre)
        self.validar_correo(correo)

        # Después se guardan los datos.
        self._identificacion = identificacion
        self._nombre = nombre
        self._correo = correo

    # Verificar que no esté vacía la identificación
    def validar_identificacion(self, identificacion):

        if identificacion == "":
            raise ClienteInvalidoError(
                "La identificación no puede estar vacía."
            )

        return True

    # Verificar que el nombre no esté vacío.
    def validar_nombre(self, nombre):

        if nombre == "":
            raise ClienteInvalidoError(
                "El nombre no puede estar vacío."
            )

        return True

    # Verificar que el correo tenga una estructura correcta
    def validar_correo(self, correo):

        if correo == "":
            raise ClienteInvalidoError(
                "El correo no puede estar vacío."
            )

        if "@" not in correo:
            raise ClienteInvalidoError(
                "El correo debe contener el símbolo @."
            )

        if "." not in correo:
            raise ClienteInvalidoError(
                "El correo debe contener un punto."
            )

        return True

    # Devolver la identificación del cliente
    def obtener_identificacion(self):

        return self._identificacion


    # Devolver el nombre
    def obtener_nombre(self):

        return self._nombre


    # Devolver el correo
    def obtener_correo(self):

        return self._correo
