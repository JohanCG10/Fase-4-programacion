"""Fase 4 - Programación UNAD | Aporte: batería de 18 simulaciones.
Autora: Angélica Esmeralda Toloza Martínez.

En el repositorio del equipo usa las clases reales cliente, servicio, reserva,
sistema, reserva_sala, alquiler_equipo y asesoria_especializada.
Si se ejecuta fuera del repositorio, utiliza un modelo autocontenido de
DEMOSTRACIÓN. No confundir los resultados de demostración con pruebas del repo.
Ejecutar: python simulaciones_angelica.py
"""
from pathlib import Path
from datetime import datetime
import csv
import logging

BASE = Path(__file__).resolve().parent
logger = logging.getLogger("SimulacionesAngelica")
logger.setLevel(logging.INFO)
logger.propagate = False
if not logger.handlers:
    fh = logging.FileHandler(BASE / "simulaciones_angelica.log", encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    logger.addHandler(fh)

try:
    from cliente import Cliente
    from sistema import Sistema
    from reserva import Reserva
    from reserva_sala import ReservaSala
    from alquiler_equipo import AlquilerEquipo
    from asesoria_especializada import AsesoriaEspecializada
    from excepciones import (ClienteInvalidoError, ServicioInvalidoError,
       ReservaInvalidaError, OperacionNoPermitidaError, ServicioNoDisponibleError)
    MODO = "INTEGRACION CON REPOSITORIO (modulos importados)"
except ImportError:
    MODO = "DEMOSTRACION LOCAL (clases internas; no valida el repositorio)"
    class ClienteInvalidoError(Exception): pass
    class ServicioInvalidoError(Exception): pass
    class ReservaInvalidaError(Exception): pass
    class OperacionNoPermitidaError(Exception): pass
    class ServicioNoDisponibleError(Exception): pass
    class Cliente:
        def __init__(self, identificacion, nombre, correo):
            if not identificacion: raise ClienteInvalidoError("Identificacion vacia")
            if not nombre: raise ClienteInvalidoError("Nombre vacio")
            if not correo or "@" not in correo or "." not in correo:
                raise ClienteInvalidoError("Correo invalido")
            self.identificacion = identificacion
        def obtener_identificacion(self): return self.identificacion
    class ServicioBase:
        def __init__(self, id_servicio, nombre, tarifa, disponible):
            if not isinstance(id_servicio, str) or not id_servicio.strip():
                raise ServicioInvalidoError("Id del servicio invalido")
            if not isinstance(nombre, str) or not nombre.strip():
                raise ServicioInvalidoError("Nombre del servicio invalido")
            if isinstance(tarifa, bool) or not isinstance(tarifa, (int,float)) or tarifa <= 0:
                raise ServicioInvalidoError("Tarifa invalida")
            if not isinstance(disponible, bool):
                raise ServicioInvalidoError("Disponibilidad invalida")
            self.sid, self.tarifa, self.disponible = id_servicio, tarifa, disponible
        def obtener_id_servicio(self): return self.sid
        def obtener_disponibilidad(self): return self.disponible
        def _verificar(self, impuesto=0, descuento=0):
            if not self.disponible: raise ServicioNoDisponibleError("Servicio no disponible")
            if impuesto < 0 or descuento < 0: raise ServicioInvalidoError("Valor negativo")
    class ReservaSala(ServicioBase):
        def __init__(self, sid, nombre, tarifa, disponible, capacidad, duracion):
            super().__init__(sid,nombre,tarifa,disponible)
            if capacidad <= 0 or duracion <= 0: raise ServicioInvalidoError("Sala invalida")
            self.duracion = duracion
        def calcular_costo(self, impuesto=0, descuento=0):
            self._verificar(impuesto,descuento)
            return self.tarifa*self.duracion*(1+impuesto/100)*(1-descuento/100)
    class AlquilerEquipo(ServicioBase):
        def __init__(self,sid,nombre,tarifa,disponible,equipo,cantidad,duracion):
            super().__init__(sid,nombre,tarifa,disponible)
            if not equipo or cantidad <= 0 or duracion <= 0:
                raise ServicioInvalidoError("Equipo invalido")
            self.cantidad,self.duracion=cantidad,duracion
        def calcular_costo(self,impuesto=0,descuento=0):
            self._verificar(impuesto,descuento)
            return self.tarifa*self.cantidad*self.duracion
    class AsesoriaEspecializada(ServicioBase):
        def __init__(self,sid,nombre,tarifa,disponible,area,duracion):
            super().__init__(sid,nombre,tarifa,disponible)
            if not area or duracion <= 0: raise ServicioInvalidoError("Asesoria invalida")
            self.duracion=duracion
        def calcular_costo(self,impuesto=0,descuento=0):
            self._verificar(impuesto,descuento)
            return self.tarifa*self.duracion
    class Reserva:
        def __init__(self,identificador,cliente,servicio):
            if not identificador or cliente is None or servicio is None:
                raise ReservaInvalidaError("Reserva incompleta")
            self.rid,self.servicio,self.estado=identificador,servicio,"Pendiente"
        def obtener_id_reserva(self): return self.rid
        def confirmar(self):
            if self.estado != "Pendiente": raise OperacionNoPermitidaError("Ya confirmada")
            if not self.servicio.obtener_disponibilidad():
                raise ServicioNoDisponibleError("No disponible")
            self.estado="Confirmada"
            return "Reserva confirmada"
    class Sistema:
        def __init__(self):
            self.clientes,self.servicios,self.reservas={},{},{}
        def agregar_cliente(self,obj):
            key=obj.obtener_identificacion()
            if key in self.clientes: raise ClienteInvalidoError("Cliente repetido")
            self.clientes[key]=obj
            return True
        def buscar_cliente(self,key): return self.clientes.get(key)
        def agregar_servicio(self,obj):
            key=obj.obtener_id_servicio()
            if key in self.servicios: raise ServicioInvalidoError("Servicio repetido")
            self.servicios[key]=obj
            return True
        def agregar_reserva(self,obj):
            key=obj.obtener_id_reserva()
            if key in self.reservas: raise ReservaInvalidaError("Reserva repetida")
            self.reservas[key]=obj
            return True
        def obtener_clientes(self): return list(self.clientes.values())

class FalloSimulacionError(Exception):
    """Error personalizado para resultados de prueba inesperados."""


def cliente_ok():
    return Cliente("1001", "Ana Lopez", "ana@example.com")


def sala_ok():
    return ReservaSala("S01", "Sala reuniones", 50000, True, 10, 2)


def asesoria_ok():
    return AsesoriaEspecializada("A01", "Asesoria Python", 50000, True, "Python", 2)


def reservar_y_confirmar():
    r = Reserva("R01", cliente_ok(), sala_ok())
    return r.confirmar()


def confirmar_dos_veces():
    r = Reserva("R02", cliente_ok(), sala_ok())
    r.confirmar()
    r.confirmar()


def confirmar_no_disponible():
    servicio = ReservaSala("S02", "Sala ocupada", 50000, False, 10, 2)
    return Reserva("R03", cliente_ok(), servicio).confirmar()


def cliente_duplicado():
    s=Sistema(); c=cliente_ok(); s.agregar_cliente(c)
    s.agregar_cliente(cliente_ok())


def servicio_duplicado():
    s=Sistema(); s.agregar_servicio(sala_ok()); s.agregar_servicio(sala_ok())


def reserva_duplicada():
    s=Sistema(); s.agregar_reserva(Reserva("R01",cliente_ok(),sala_ok()))
    s.agregar_reserva(Reserva("R01",cliente_ok(),sala_ok()))


def alta_y_busqueda():
    s=Sistema(); s.agregar_cliente(cliente_ok())
    assert s.buscar_cliente("1001") is not None, "No se recupera el cliente"
    return True

CASOS = [
    ("01", "Cliente valido", cliente_ok, None),
    ("02", "Identificacion vacia", lambda: Cliente("", "Ana", "ana@example.com"), ClienteInvalidoError),
    ("03", "Correo sin arroba", lambda: Cliente("1002", "Ana", "anacorreocom"), ClienteInvalidoError),
    ("04", "Sala valida: calcular costo", lambda: sala_ok().calcular_costo(), None),
    ("05", "Tarifa negativa", lambda: ReservaSala("S03", "Sala", -50, True, 10, 2), ServicioInvalidoError),
    ("06", "Servicio no disponible", lambda: ReservaSala("S04","Ocupada",50000,False,10,2).calcular_costo(), ServicioNoDisponibleError),
    ("07", "Asesoria valida", lambda: asesoria_ok().calcular_costo(), None),
    ("08", "Impuesto negativo", lambda: asesoria_ok().calcular_costo(impuesto=-19), ServicioInvalidoError),
    ("09", "Equipo cantidad negativa", lambda: AlquilerEquipo("E01","Portatiles",30000,True,"Portatil",-1,2), ServicioInvalidoError),
    ("10", "Registro y consulta de cliente", alta_y_busqueda, None),
    ("11", "Cliente duplicado", cliente_duplicado, ClienteInvalidoError),
    ("12", "Servicio duplicado", servicio_duplicado, ServicioInvalidoError),
    ("13", "Reserva sin cliente", lambda: Reserva("R04",None,sala_ok()), ReservaInvalidaError),
    ("14", "Reserva sin servicio", lambda: Reserva("R05",cliente_ok(),None), ReservaInvalidaError),
    ("15", "Reserva valida y confirmada", reservar_y_confirmar, None),
    ("16", "Confirmacion duplicada", confirmar_dos_veces, OperacionNoPermitidaError),
    ("17", "Confirmacion de servicio ocupado", confirmar_no_disponible, ServicioNoDisponibleError),
    ("18", "Reserva duplicada en sistema", reserva_duplicada, ReservaInvalidaError),
]


def ejecutar_caso(numero, descripcion, accion, esperado):
    """try/except/else/finally, logs y encadenamiento cuando hay fallo inesperado."""
    try:
        accion()
    except Exception as exc:
        logger.warning("CASO %s - excepcion detectada %s: %s", numero, type(exc).__name__, exc)
        if esperado is not None and isinstance(exc, esperado):
            return "APROBADO", "Se controlo el error esperado"
        raise FalloSimulacionError(f"Excepcion inesperada en {numero}") from exc
    else:
        if esperado is not None:
            raise FalloSimulacionError(f"Se esperaba {esperado.__name__} y no ocurrio")
        logger.info("CASO %s - operacion valida", numero)
        return "APROBADO", "Operacion completada sin error"
    finally:
        logger.info("Fin del caso %s: %s", numero, descripcion)


def main():
    logger.info("INICIO | %s | %s", datetime.now().isoformat(), MODO)
    print("FASE 4 - SIMULACIONES DE ANGELICA TOLOZA")
    print("MODO:", MODO)
    resultados=[]
    for n, desc, accion, esperado in CASOS:
        try:
            estado, detalle = ejecutar_caso(n, desc, accion, esperado)
        except FalloSimulacionError as exc:
            estado, detalle = "FALLIDO", str(exc)
            logger.exception("CASO %s FALLIDO: %s", n, desc)
        except Exception as exc:
            estado, detalle = "FALLIDO", f"Fallo imprevisto: {type(exc).__name__}: {exc}"
            logger.exception("CASO %s FALLIDO: %s", n, desc)
        resultados.append((n, desc, estado, detalle))
        print(f"{n} | {estado:8} | {desc}")
    archivo=BASE / "resultados_simulaciones_angelica.csv"
    with archivo.open("w",encoding="utf-8-sig",newline="") as f:
        writer=csv.writer(f,delimiter=";")
        writer.writerow(["Caso","Descripcion","Estado","Detalle"])
        writer.writerows(resultados)
    total=sum(1 for x in resultados if x[2]=="APROBADO")
    print(f"RESUMEN: {total}/{len(CASOS)} casos aprobados")
    print("ARCHIVOS: simulaciones_angelica.log y resultados_simulaciones_angelica.csv")
    logger.info("FIN | %s/%s aprobados",total,len(CASOS))
    return total==len(CASOS)


if __name__=="__main__":
    main()
