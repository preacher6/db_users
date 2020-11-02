
from pymongo import MongoClient

client = MongoClient('localhost')

database_ = client['prueba']

coleccion = database_['usuarios']

""" coleccion.insert_many([{'edad':14, 'nombre':'ajuli', 'interes': ['viejas']},
                        {'edad':65, 'nombre':'olo', 'interes': ['hockey']},
                        {'edad':23, 'nombre':'arty', 'interes': ['computo']}]) """

for documento in coleccion.find({'edad':{"$gt":14}}):
    print(documento)
