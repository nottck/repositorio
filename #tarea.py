#tarea
edad=int(input("ingrese su edad"))
if edad >= 18:
  print("Eres mayor de edad")

else:
  print("Eres menor de edad")

user1=input(print("\ningrese el usuario:"))
pwd1=input(print("ingrese la contraseña:"))

if (user1== "pedro" or user1== "angel") and (pwd1== "1234" or pwd1== "a4s1"):
 print("El Usuario esta registrado")

else:
  print("El usuario no esta resgitrado")

nota1=float(input("\ningrese la nota 1:"))

nota2=float(input("ingrese la nota 2:"))

nota3=float(input("ingrese la nota 3:"))

promedio=nota1+nota2+nota3/3

if  promedio >= 4:
  print("Aprobado")

else:
   print("No estas aprobado")

print("\nOpciones de animales")
print("perro")
print("Cocodrilo")
print("Conejo")
print("Tiburon")

opcion=input("¿Cuál de los siguientes animales vive en el agua?")
if opcion=="Cocodrilo":
  print("+0.5 a tu puntaje")

elif opcion=="Tiburon":
    print("+1 a tu puntaje")

else:
      ("Error ese animal no vive en el agua")


puntaje = 0


preguntas = [

    ("¿Cuántos lados tiene un triángulo?", ["3", "4", "5"], "1"),

    ("¿Cuál es el planeta más cercano al sol?", ["Marte", "Venus", "Mercurio"], "3"),

    ("¿Cuántos continentes hay en el mundo?", ["5", "6", "7"], "3")

]

for pregunta, opciones, correcta in preguntas:
    print("\n" + pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    if input("Elige una opción (1, 2 o 3): ") == correcta:

        puntaje += 1

calificaciones = ["Necesitas repasar más.", "Podrías mejorar.", "Muy bien.", "¡Excelente!"]

print(f"\nTu puntaje obtenido es: {puntaje} puntos. {calificaciones[puntaje]}")