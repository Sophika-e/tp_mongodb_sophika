# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sqlite3 import Date

from pymongo import MongoClient
import datetime

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
# donner la database
esmeDB = client['supermarche']
produit = esmeDB['produit']
commande = esmeDB['commande']
inventaireproduit = esmeDB['inventaireproduit']
caisse = esmeDB['caisse']

inventaireproduit1 = {"_id": "1", "nom": "courgette", "nb_restant": 9}
inventaireproduit2 = {"_id": "2", "nom": "tomate", "nb_restant": 13}
inventaireproduit3 = {"_id": "3", "nom": "pate", "nb_restant": 5}
inventaireproduit4 = {"_id": "4", "nom": "poulet", "nb_restant": 9}

produit1 = {"_id": "1", "nom": "courgette", "description": "legume", "quantite": [inventaireproduit1]}
produit2 = {"_id": "2", "nom": "tomate", "description": "legume", "quantite": [inventaireproduit2]}
produit3 = {"_id": "3", "nom": "pate", "description": "bio, complet", "quantite": [inventaireproduit3]}
produit4 = {"_id": "4", "nom": "poulet", "description": "viande, poulet roti", "quantite": [inventaireproduit4]}

commande1 = {"_id": "1", "contenu": [produit1, produit2], "date": "13/04/2021"}
commande2 = {"_id": "2", "contenu": [produit4, produit3], "date": "13/04/2021"}
commande3 = {"_id": "3", "contenu": [produit3, produit1], "date": "13/04/2021"}
commande4 = {"_id": "4", "contenu": [produit4, produit2, produit3], "date": "13/04/2021"}

"""
produits= [produit1,produit2,produit3,produit3]
print (produit.insert_many(produits))"""

caisse1 = {"_id": "1", "commande": [commande1, commande3]}
caisse2 = {"_id": "2", "commande": [commande2, commande4]}
caisse3 = {"_id": "3", "commande": [commande3, commande4]}

"""
x1=caisse.insert_one(caisse1)
x2=caisse.insert_one(caisse2)
x3=caisse.insert_one(caisse3)

print(x1)
print(x2)
print(x3)"""


"""
x1 = inventaireproduit.insert_one(inventaireproduit1)
x2 = inventaireproduit.insert_one(inventaireproduit2)
x3 = inventaireproduit.insert_one(inventaireproduit3)
x4 = inventaireproduit.insert_one(inventaireproduit4)
print(x1)
print(x2)
print(x3)
print(x4)
"""

"""
x1=produit.insert_one(produit1)
x2=produit.insert_one(produit2)
x3=produit.insert_one(produit3)
x4=produit.insert_one(produit4)

print(x1)
print(x2)
print(x3)
print(x4)"""

"""
x1=commande.insert_one(commande1)
x2=commande.insert_one(commande2)
x3=commande.insert_one(commande3)
x4=commande.insert_one(commande4)

print(x1)
print(x2)
print(x3)
print(x4)
"""

x1 = produit.insert_one(produit1)
x2 = produit.insert_one(produit2)
x3 = produit.insert_one(produit3)
x4 = produit.insert_one(produit4)

print(x1)
print(x2)
print(x3)
print(x4)



