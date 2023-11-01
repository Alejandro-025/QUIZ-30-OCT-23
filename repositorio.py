#Quiz del ciclo for en python
#Usando for y una lista con sus notas, calcule su nota definitiva hasta la fecha

notas= [50, 50, 45, 47, 0, 40]
porcentajes=[0.05, 0.1, 0.2, 0.06, 0.06, 0.03]

nota_fecha = 0

for i in range(len(notas)):
    nota_fecha +=notas[i] * porcentajes[i]

print("Mi nota hasta la fecha es:", nota_fecha)


#len: proporciona el numero de elementos para que sea leido uno por uno y lo multimplica por los elementos de la otra lista en orden.