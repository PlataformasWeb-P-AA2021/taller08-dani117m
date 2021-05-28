from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generador_tabla import mundial

from csv import reader
import requests


# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///mundial2018.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

leer_mundial = open('data/mundial2018.csv', 'r', encoding="utf-8")
jugadores = list(leer_mundial)

lectura_est = []


print(jugadores[1])

for d in range(0, len(jugadores),1):
    i = jugadores[d].split("|")
    p = mundial(numero=i[0], fifaDis=i[1], country=i[2], lastName=i[3], firstName=i[4],\
    shirtName=i[5], pos=i[6], height=i[7], caps=i[8], goals=i[9])
    session.add(p)

# confirmar transacciones
##print (datos_mundial)

session.commit()

