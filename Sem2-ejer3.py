cant = input("Ingrese cantidad de asignaturas: ")
lista_asignatura = []
notas = []

def registro_notas(c):
    for i in range(int(c)):
        asignatura = input("Ingrese el nombre de la asignatura: ")
        lista_asignatura.append(asignatura)
        nota = input("Ingrese la nota de la asignatura: ")
        notas.append(nota)

def reporte_notas(lista1, lista2):
    for i in range(len(lista1)):
        mensaje= "En {} has sacado {}".format(lista1[i], lista2[i])
        print(mensaje)

registro_notas(cant)
reporte_notas(lista_asignatura, notas)