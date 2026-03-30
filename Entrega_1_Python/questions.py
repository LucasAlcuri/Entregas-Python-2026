import random
programacion = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
    ]

marca_autos = [
    "audi",
    "bmw",
    "ferrari",
    "alpharomeo",
    "toyota",
    "cadilac",
    "chevrolet",
    "renault",
]

apellidos_futbol = [
    "messi",
    "maradona",
    "batistuta",
    "riquelme",
    "aguero",
    "mascherano",
    "dybala",
]

entrada = int (input("Ingrese el numero la categoria con la que desea jugar:" "\n"
               "1.Programacion" "\n"
               "2.Marca Autos" "\n"
               "3.Apellidos de futbol" "\n"))
match entrada:
        case 1:
            palabras = random.sample(programacion, k=len(programacion))
        case 2:
            palabras = random.sample(marca_autos, k=len(marca_autos))
        case 3:
            palabras = random.sample(apellidos_futbol, k=len(apellidos_futbol))

ronda = 1
puntaje_total = 0

print("¡Bienvenido al Ahorcado!")

for word in palabras:
   
    guessed = []
    attempts = 6
    print() 
    print("Ronda numero",ronda)
    print()

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            attempts += 6
            puntaje_total += attempts
            ronda += 1
            print("¡Ganaste!")
            print("Tu puntaje fue de",attempts,"puntos!")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        
        letter = input("Ingresá una letra: ")
        
        #Verifica que el caracter sea valido
        while True:
            if len(letter) > 1 or not letter.isalpha():
                print("Caracter invalido intente de nuevo")
                letter = input("Ingresá una letra: ")
            else:
                break    

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
        
        print()
        
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        print("Tu puntaje fue de",attempts,"puntos!")
        ronda += 1
    
    seguir = input("¿Querés seguir? (s/n): ")
    if seguir.lower() != "s":
        break
    

print()
print("Fin del juego!")
print("Puntaje Total:",puntaje_total)