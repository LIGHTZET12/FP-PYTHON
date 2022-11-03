# -- coding: utf-8 --
### ZONA DE IMPORTS
import csv
from collections import namedtuple
from datetime import datetime

#NAMEDTUPLE

Paciente= namedtuple("paciente", "cod_paciente, colesterol, trigliceridos, hemoglobina, sexo, fecha")


def lee_fichero(fichero):
    """
    Funcion de lectura del fichero csv
    
    input: fichero de texto.
    
    output=[(str,int,int,float,str,date)]
    
    """
    registros=[]

    with open(fichero,encoding="utf-8") as f:
        lector=csv.reader(f,delimiter=",")
        next(lector)
        

        for cod_paciente, colesterol, trigliceridos, hemoglobina, sexo, fecha in lector: 
            colesterol=int(colesterol) 
            trigliceridos=int(trigliceridos) 
            hemoglobina = float(hemoglobina)
            fecha=parsea_fecha(fecha)
            tupla=Paciente(cod_paciente, colesterol, trigliceridos, hemoglobina, sexo, fecha)
            registros.append(tupla)
            
    return registros
            
            
            
            
def parsea_fecha(str_fecha):
    return datetime.strptime(str_fecha.strip(), "%d/%m/%Y").date()