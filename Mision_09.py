def extraerPares(lista):
	valor={}
	for item in lista:
		if(item%2==0):
			valor.add(item)
	return valor

def extraerMayoresPrevio(lista):
	valor = []
	for x in range(1,len(lista)):
		if(lista[x]>lista[x-1]):
			valor.append(lista[x])
	return valor

def intercambiarParejas(lista):
	valor = []
	for x in range(0,len(lista),2):
		if(x+1>=len(lista)):
			valor.append(lista[x])
		else:
			valor.append(lista[x+1])
			valor.append(lista[x])
	return valor

def intercambiarMM(lista):
	indxMin = -1
	indxMax = -1
	cont=0
	minimo = 9999
	maximo = 0
	for x in lista:
		if(x<minimo):
			minimo =x
			indxMin =cont
		elif(x>maximo):
			maximo =x
			indxMax = cont
		cont+=1
	lista[indxMax]=minimo
	lista[indxMin]=maximo
	return lista

def promedioCentro(lista):
	minimo = 9999
	maximo = 0
	suma=0
	cont = 0
	for x in lista:
		if(x<minimo):
			minimo =x
		elif(x>maximo):
			maximo =x
		suma+=x
		cont+=1
	suma=suma-maximo-minimo
	return suma//(cont-2)

def calcularEstadistica(lista):
	mean = (sum(lista)/len(lista))
	valor = []
	for x in lista:
		valor.append((x-mean)**2)
	stddev = (sum(valor)/len(valor))**(1/2)
	result=(mean,stddev)
	return result

def calcularSuma(lista):
	suma = 0
	for x in range(len(lista)):
		if(lista[x]==13):
			if(x>0):
				suma= suma - lista[x-1]
			if(x+1<len(lista)):
				suma= suma - lista[x+1]
		else:
			suma+=lista[x]
	return suma