import nltk 
from nltk.metrics.distance import jaro_similarity
import numpy as np

mediated = ["UID", "name", "CCInfo", "PID", "OID", "OID", "UID", "orderNumber", "totalCost", "Adress", "PID", "pizzaName", "nutrition", "price"]

s1s2 = ["SOPID", "PizzaName", "nurishment", "total", "CID", "PIID", "FirstName", "LastName", "PIID", "CreditCardNumber", "ccv", "expDate", "OID", "CID", "orderCode", "totalAmount", "Adress", "PID", "OID", "PID", "title", "nurishment", "price", "UID", "FirstName", "LastName", "CCNumber", "ccv", "expDate", "OID", "UID", "orderNumber", "Sum", "AID", "OID", "PID", "AID", "User", "street", "city", "zip"]


matEdit = nltk.edit_distance(mediated, s1s2)
#newMat = np.arange(mediated)
lev=np.zeros((len(mediated), len(s1s2)))
#print(newMat)
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(s1s2)):
		lev[wordI, wordJ] = nltk.edit_distance(mediated[wordI], s1s2[wordJ])

jaro=np.zeros((len(mediated), len(s1s2)))
#print(newMat)
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(s1s2)):
		jaro[wordI, wordJ] = jaro_similarity(mediated[wordI], s1s2[wordJ])

jaccard=np.zeros((len(mediated), len(s1s2)))
#print(newMat)
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(s1s2)):
		jaccard[wordI, wordJ] = nltk.jaccard_distance(set(mediated[wordI]), set(s1s2[wordJ]))


print(jaccard)