import numpy as np
import matplotlib.pyplot as plt
#Aqui obtenemos los datos de modo String. Observando el archivo, tenemos que en la columna 2 son los datos de la forma M/B
datos = np.genfromtxt("WDBC.dat", dtype = str, delimiter = ",")
numeroCol = len(datos[0,:])
numeroFil = len(datos[:,0])
#Convertiremos la columna 2 en un arreglo tipo float. M = 0 y B = 1
for i in range(len(datos[:,1])):
		if(datos[i,1] == "M"):
			datos[i,1] = 0.0
		elif(datos[i,1] == "B"):
			datos[i,1] = 1.0
#Pasamos todos los datos a tipo float
datosModificados = np.empty((numeroFil,numeroCol))		
for i in range(numeroCol):
	for j in range(numeroFil):
		datosModificados[j,i] = float(datos[j,i])
#Con los datos obtenidos, procedemos al ejercicio PCR. Creemos un vector de promedios para cada columna
vectorPromedio = np.zeros(numeroCol)
for i in range(numeroCol):
	vectorPromedio[i] = datosModificados[:,i].sum()/numeroFil
print vectorPromedio[26] - datosModificados[:,26].mean()



