datos = {"codigo": ["E-001", "E-002", "E-003", "E-004", "E-005"],
         "nombre": ["Alexander", "Luis", "Juan", "Mateo", "Ruben"],
         "cursos": ["Algebra", "Comunicacion", "Quimica", "Matematica", "Historia"]}
nota = []
resp = "s"
while resp == "s":
    codigo = input("Ingrese el codigo del alumno: ")
    curso = input("Ingresar el area: ")
    nota1 = int(input("Ingresar la primera nota del alumno: "))
    nota2 = int(input("Ingresar la segunda nota del alumno: "))
    nota3 = int(input("Ingresar la tercera nota del alumno: "))
    nota4 = int(input("Ingresar la cuarta nota del alumno: "))
    x = 0
    for i in datos ["codigo"]:
        if i == codigo:
            codigotemp = 1
            nombretemp = datos ["nombre"][x]

            promedio = (nota1 + nota2 + nota3 + nota4)/4
            registro = ["codigo: " + str(codigotemp) + " | " + "nombre: " + str(nombretemp) + " | " + "curso: " + curso + " | " + "promedio: " + str(promedio) + " | " + "nota1: " + str(nota1) + " | " + "nota2: " + str(nota2) + " | " + "nota3: " + str(nota3) + " | " + "nota4: " + str(nota4)]
            f = open("examen_final.txt", "a")
            cadena = "".join(registro)
            f.write("\n" +  cadena)
            f.close()
        x += 1
    resp = input("¿Desea continuar ingresando datos? : s/n : ")
    f = open("examen_final.txt")
    print(f.read())
    f.close()