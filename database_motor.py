from pymongo import MongoClient, ASCENDING, DESCENDING

client = MongoClient('localhost')

database_ = client['prueba']

coleccion = database_['usuarios']

# Insertar varios elementos
""" coleccion.insert_many([{'edad':14, 'nombre':'ajuli', 'interes': ['viejas']},
                        {'edad':65, 'nombre':'olo', 'interes': ['hockey']},
                        {'edad':23, 'nombre':'marty', 'interes': ['computo']}]) """

# Realizar consultas 
for documento in coleccion.find({'edad':{"$gte":10}}):
    print(documento)

#print(coleccion.find_one({'edad':{"$gt":24}}))

# Eliminar elementos
""" coleccion.delete_many({'edad':{"$lte":20}})
coleccion.delete_one({'edad': {'$gte':65}}) """

# Actualizar elementos
#coleccion.update_one({"edad":{"$lt":40}}, {"$set":{"edad":50}})
#coleccion.create_index([('edad', ASCENDING)])

# Eliminar coleccion
#database_.drop_collection('usuarios')

# Eliminar base de datos
client.drop_database('prueba')
print(client.list_database_names())