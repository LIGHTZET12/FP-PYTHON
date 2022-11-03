# -- coding: utf-8 --
from codigo import *



def test_lee_fichero():
    print("Se han obtenido", len(fichero),"analisis")
    print(fichero)
    


if __name__ == '__main__':
    fichero=lee_fichero('./Entrega2022Python/data/estudio_pacientes.csv')
    test_lee_fichero()