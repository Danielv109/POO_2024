
from Coches import *

# print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
coche1.getInfo()

# print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",180,150,6)
coche2.getInfo()

#print("Objeto 3")
camion1 = camiones("Negro","Dina","2020",180,300,12,8,2500)
camion1.getInfo()

#print("Objeto 4")
camion2 = camiones("Azul","Star","2019",150,300,14,6,2000)
camion2.getInfo()

#print("Objeto 5")
camioneta1 = camionetas("Amarillo","Renault","2025",1240,250,8,"delantera",True)
camioneta1.getInfo()

#print("Objeto 6")
camioneta2 = camionetas("Blanca","Nissan","2020",180,150,6,"trasera",False)
camioneta2.getInfo()


# print(coche1.publico_atributo)
# print(coche1.__privado_atributo) esto no es permitido
