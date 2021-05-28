from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from generador_tabla import mundial

# se importa información del archivo configuracion
##from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///mundial2018.db')

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 

jugadores = session.query(mundial).order_by(mundial.height.desc()).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("ordenados por la estatura")
for s in jugadores:
    ##print("%s" % (s))
    print("-----------------------------------------------")
    print("Nombre: %s altura: %s" % (s.fifaDis, s.height))
# Obtener todos los registros de 


