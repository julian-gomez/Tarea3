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
#Crearemos una nueva matriz con la diferencia de los promedios
matrizNueva = np.zeros((numeroFil, numeroCol))
for i in range(numeroCol):
	matrizNueva[:,i] = datosModificados[:,i] - vectorPromedio[i]
matrizCovarianza = np.zeros((numeroCol,numeroCol))

for i in range(numeroCol):
	for j in range(numeroCol):
		a = ((matrizNueva[:,i]*matrizNueva[:,j]).sum())/(numeroFil-1)
		matrizCovarianza[i,j] = a
#Imprimimos la matriz de Covarianza
print matrizCovarianza
print "### Separador ###"
#Ahora, comparamos con la funcion de numpy
print matrizCovarianza - np.cov(matrizNueva.T)
print "### Separador ###"

#Ahora, vamos a calcular los valores y vetores propios

valoresPropios = np.linalg.eigvals(matrizCovarianza)
vectoresPropios = np.linalg.eig(matrizCovarianza)[1]

for i in range(len(valoresPropios)):
	print "Valor propio ", valoresPropios[i], " Con vector propio ", vectoresPropios[i]
#Ahora, usando como referencia el archivo del siguiente link: www.cs.otago.ac.nz/cosc453/student_tutorials/principal_components.pdf podemos realizar los siguientes puntos. Notese que la funcion eigvalues imprime los valores propios de mayor a menor, por tanto usamos esots vectores propios como PC1 y PC2 respectivamente.

print "### Separador ###"

print "PC1: ", vectoresPropios[0]
print "PC2: ", vectoresPropios[1]

