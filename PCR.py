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
#Con los datos obtenidos, procedemos al ejercicio PCA. Creemos un vector de promedios para cada columna (Exceptuando las dos primeras)
vectorPromedio = np.zeros(numeroCol - 2)
for i in range(numeroCol -2):
	vectorPromedio[i] = datosModificados[:,i + 2].sum()/numeroFil
#Crearemos una nueva matriz con la diferencia de los promedios
matrizNueva = np.zeros((numeroFil, numeroCol - 2))
for i in range(numeroCol - 2):
	matrizNueva[:,i] = datosModificados[:,i + 2] - vectorPromedio[i]
matrizCovarianza = np.zeros((numeroCol - 2,numeroCol - 2))

for i in range(numeroCol - 2):
	for j in range(numeroCol - 2):
		a = ((matrizNueva[:,i]*matrizNueva[:,j]).sum())/(numeroFil-1)
		matrizCovarianza[i,j] = a
#Imprimimos la matriz de Covarianza
print matrizCovarianza
print "### Separador ###"
"""
#Ahora, comparamos con la funcion de numpy
print matrizCovarianza - np.cov(matrizNueva.T)
print "### Separador ###" """

#Ahora, vamos a calcular los valores y vetores propios

valoresPropios = np.linalg.eigvals(matrizCovarianza)
vectoresPropios = np.linalg.eig(matrizCovarianza)[1]

for i in range(len(valoresPropios)):
	print "Valor propio ", valoresPropios[i], " Con vector propio ", vectoresPropios[i]
#Ahora, usando como referencia el archivo del siguiente link: www.cs.otago.ac.nz/cosc453/student_tutorials/principal_components.pdf podemos realizar los siguientes puntos. Notese que la funcion eigvalues imprime los valores propios de mayor a menor, por tanto usamos estos vectores propios como PC1 y PC2 respectivamente.

print "### Separador ###"
print "PC1: ", vectoresPropios[0]
print "PC2: ", vectoresPropios[1]
print "### Separador ###"

#Creamos una matriz con estos vectores
matrizVectoresPCA = np.zeros((numeroCol - 2,2))
matrizVectoresPCA[:,0] = vectoresPropios[0]
matrizVectoresPCA[:,1] = vectoresPropios[1]

#Ahora, vamos a separar en 2 matrices los datos con M y los datos con B. Usaremos de nuevo la matriz datos modificados (M = 0 y B = 1)

numeroM = 0
numeroB = 0

for i in range(numeroFil):
	if(datosModificados[i,1] == 0.0):
		numeroM += 1
	elif(datosModificados[i,1] == 1.0):
		numeroB += 1
matrizPacientesM = np.zeros((numeroM, numeroCol - 2))
matrizPacientesB = np.zeros((numeroB, numeroCol - 2))


for i in range(numeroM):
	if(datosModificados[i,1] == 0.0):
		matrizPacientesM[i,:] = datosModificados[i,2:numeroCol]
for i in range(numeroB):
	if(datosModificados[i,1] == 1.0):
		matrizPacientesB[i,:] = datosModificados[i,2:numeroCol]

#Ahora, haremos el producto entre cada fila de nuestras nuevas matrices y la matriz de vectores propios definida antes

matriz_2X2M = np.zeros((numeroM,2))
matriz_2X2B = np.zeros((numeroB,2))

for i in range(numeroM):
	matriz_2X2M[i,:] = matrizPacientesM[i,:].dot(matrizVectoresPCA)
for i in range(numeroB):
	matriz_2X2B[i,:] = matrizPacientesB[i,:].dot(matrizVectoresPCA)

plt.figure()

plt.scatter(matriz_2X2M[:,0], matriz_2X2M[:,1], label = "M")
plt.scatter(matriz_2X2B[:,0], matriz_2X2B[:,1], label = "B")
plt.legend()
plt.savefig("CalderonJulian_PCA.pdf")

print "Observando la grafica, el metodo de PCA parece bastante util en separar el conjunto de malignos respecto al de benignos, mostrando una tendencia a agrupar los malignos en una region menor que los benignos. Con esta separacion es posible desarrollar un estudio mas objetivo sobre los pacientes. Existe alguna medicion que sobresale en un conjunto mas que el otro."





















