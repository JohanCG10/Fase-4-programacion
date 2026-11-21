import logging


# Configuración del archivo donde se guardarán
# los eventos y errores del programa.
logging.basicConfig(
    filename="sistema_fj.log",
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    ),
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8"
)


# Se crea el objeto que permitirá registrar los mensajes.
logger = logging.getLogger("SoftwareFJ")