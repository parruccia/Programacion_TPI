def san_martin():
   print("Juego de Elección: Cruce de los Andes de San Martín")

# Introducción
   print("Año 1817. Eres el líder del Ejército de los Andes, José de San Martín.")
   print("Debes tomar decisiones críticas para cruzar los Andes y liberar Chile.")

# Variable para almacenar la salud del ejército
   salud_ejercito = 100

# Variable para almacenar la moral del ejército
   moral_ejercito = 100

# Etapa 1: Preparación
   print(" Etapa 1: Preparación")
   print("Debes elegir un lugar para acampar y preparar al ejército.")
   print("A) Mendoza")
   print("B) San Juan")
   print("C) La Rioja")
   print("D) San Luis")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
       print("Excelente elección. Mendoza es un lugar estratégico.")
       salud_ejercito += 10
       print("Salud del ejercito + 10")
       moral_ejercito += 10
       print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
       print("Buena elección. San Juan ofrece recursos naturales.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
       print("Mala elección. La Rioja es un lugar peligroso.")
       salud_ejercito -= 10
       print("Salud del ejercito - 10")
       moral_ejercito -= 10
       print("Moral del ejercito + 10")
   elif eleccion.upper() == "D":
       print("Buena elección. San Luis ofrece una posición defensiva.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   else:
       print("Opción inválida.")

# Etapa 2: Cruce de los Andes
   print(" Etapa 2: Cruce de los Andes")
   print("Debes elegir una ruta para cruzar los Andes.")
   print("A) Ruta del Portillo")
   print("B) Ruta de Uspallata")
   print("C) Ruta de Los Patos")
   print("D) Ruta de Villalobos")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
       print("Excelente elección. La ruta del Portillo es segura.")
       salud_ejercito += 10
       print("Salud del ejercito + 10")
       moral_ejercito += 10
       print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
       print("Buena elección. La ruta de Uspallata es rápida.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
       print("Mala elección. La ruta de Los Patos es peligrosa.")
       salud_ejercito -= 10
       print("Salud del ejercito - 10")
       moral_ejercito -= 10
       print("Moral del ejercito - 10")
   elif eleccion.upper() == "D":
       print("Buena elección. La ruta de Villalobos es sorprendente.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   else:
       print("Opción inválida.")

# Etapa 3: Batalla de Chacabuco
   print(" Etapa 3: Batalla de Chacabuco")
   print("Debes elegir una estrategia para la batalla.")
   print("A) Ataque frontal")
   print("B) Flanqueo")
   print("C) Retirada")
   print("D) Emboscada")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
       print("Excelente elección. El ataque frontal es efectivo.")
       salud_ejercito += 10
       print("Salud del ejercito + 10")
       moral_ejercito += 10
       print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
       print("Buena elección. El flanqueo es sorprendente.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
       print("Mala elección. La retirada es cobardía.")
       salud_ejercito -= 10
       print("Salud del ejercito - 10")
       moral_ejercito -= 10
       print("Moral del ejercito - 10")
   elif eleccion.upper() == "D":
       print("Buena elección. La emboscada es efectiva.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   else:
       print("Opción inválida.")

# Etapa 4: Avance hacia Santiago
   print(" Etapa 4: Avance hacia Santiago")
   print("Debes elegir una ruta para avanzar hacia Santiago.")
   print("A) Ruta directa por la carretera")
   print("B) Ruta alternativa por los cerros")
   print("C) Ruta fluvial por el río Mapocho")
   print("D) Ruta de infiltración en la noche")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
      print("Excelente elección. La ruta directa es rápida.")
      salud_ejercito += 10
      print("Salud del ejercito + 10")
      moral_ejercito += 10
      print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
      print("Buena elección. La ruta alternativa es segura.")
      salud_ejercito += 5
      print("Salud del ejercito + 5")
      moral_ejercito += 5
      print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
      print("Mala elección. La ruta fluvial es lenta.")
      salud_ejercito -= 10
      print("Salud del ejercito - 10")
      moral_ejercito -= 10
      print("Moral del ejercito - 10")
   elif eleccion.upper() == "D":
      print("Buena elección. La ruta de infiltración es sorprendente.")
      salud_ejercito += 5
      print("Salud del ejercito + 5")
      moral_ejercito += 5
      print("Moral del ejercito + 5")
   else:
      print("Opción inválida.")

# Etapa 5: Batalla de Maipú
   print(" Etapa 5: Batalla de Maipú")
   print("Debes elegir una estrategia para la batalla.")
   print("A) Ataque frontal")
   print("B) Flanqueo")
   print("C) Retirada")
   print("D) Emboscada")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
      print("Excelente elección. El ataque frontal es efectivo.")
      salud_ejercito += 10
      print("Salud del ejercito + 10")
      moral_ejercito += 10
      print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
      print("Buena elección. El flanqueo es sorprendente.")
      salud_ejercito += 5
      print("Salud del ejercito + 5")
      moral_ejercito += 5
      print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
      print("Mala elección. La retirada es cobardía.")
      salud_ejercito -= 10
      print("Salud del ejercito - 10")
      moral_ejercito -= 10
      print("Moral del ejercito - 10")
   elif eleccion.upper() == "D":
      print("Buena elección. La emboscada es efectiva.")
      salud_ejercito += 5
      print("Salud del ejercito + 5")
      moral_ejercito += 5
      print("Moral del ejercito + 5")
   else:
      print("Opción inválida.")

# Resultado final
   print("Resultado final:")
   print("Salud del ejército:", salud_ejercito)
   print("Moral del ejército:", moral_ejercito)

   if salud_ejercito > 80 and moral_ejercito > 80:
      print("¡Felicidades! Has ganado la campaña y liberado Chile.")
   else:
      print("Lo siento. Has perdido la campaña y el ejército está debilitado.")

   print("Fin de la historia")
def preguntados():

    import json
    import random

    # Cargar preguntas desde el archivo JSON
    with open('C:/Users/Ignacio/Desktop/CARPETA FINAL/preguntas_preguntados.json', 'r', encoding='utf-8') as file:
        preguntas_por_categoria = json.load(file)

    # Inicializamos puntajes de los jugadores en 0
    puntaje_1 = 0
    puntaje_2 = 0

    # Inicializar la lista de preguntas usadas para no repetirlas
    preguntas_usadas_1 = []
    preguntas_usadas_2 = []

    # Mensaje inicial
    print("""                                                                                                  
     #####    #####    ######    #####   ##  ##   ##  ##   ######     ##     ####      ####     ####
     ##  ##   ##  ##   ##       ##       ##  ##   ### ##     ##      ####    ## ##    ##  ##   ##
     ##  ##   ##  ##   #####    ##       ##  ##   ######     ##     ##  ##   ##  ##   ##  ##    ####
     #####    #####    ##       ## ###   ##  ##   ######     ##     ##  ##   ##  ##   ##  ##       ##
     ##       ## ##    ##       ##  ##   ##  ##   ## ###     ##     ######   ## ##    ##  ##       ##
     ##       ##  ##   ######    #####   ######   ##  ##     ##     ##  ##   ####      ####     ####  

                                        PARA COMENZAR INGRESE "1"                                                                                                                                                                                      
    """)

    start = int(input())

    if start == 1:
        # Ingreso de nombres de jugadores
        jugador1 = input("Ingrese el nombre del jugador 1: ")
        jugador2 = input("Ingrese el nombre del jugador 2: ")

        # Comienzo del juego
        while puntaje_1 < 6 and puntaje_2 < 6:
            # Turno del jugador 1
            print(f"Turno de {jugador1}")
            while True:
                categoria_actual = random.choice(list(preguntas_por_categoria.keys()))
                preguntas_no_usadas = [
                    pregunta for pregunta in preguntas_por_categoria[categoria_actual] if pregunta not in preguntas_usadas_1
                ]

                if not preguntas_no_usadas:
                    print(f"No hay más preguntas disponibles en la categoría {categoria_actual} para {jugador1}")
                    continue

                pregunta_aleatoria = random.choice(preguntas_no_usadas)
                preguntas_usadas_1.append(pregunta_aleatoria)

                print(f"Categoría: {categoria_actual}")
                print(pregunta_aleatoria["pregunta"])
                for opcion in pregunta_aleatoria["opciones"]:
                    print(opcion)

                respuesta_usuario = input("¿Cuál es tu respuesta? (A/B/C/D): ").upper()

                if respuesta_usuario == pregunta_aleatoria["respuesta"]:
                    print("¡Correcto!")
                    puntaje_1 += 1
                    break
                else:
                    print("¡Incorrecto!")
                    break

            print(f"{jugador1} tiene {puntaje_1} puntos.\n")

            # Turno del jugador 2
            print(f"Turno de {jugador2}")
            while True:
                categoria_actual = random.choice(list(preguntas_por_categoria.keys()))
                preguntas_no_usadas = [
                    pregunta for pregunta in preguntas_por_categoria[categoria_actual] if pregunta not in preguntas_usadas_2
                ]

                if not preguntas_no_usadas:
                    print(f"No hay más preguntas disponibles en la categoría {categoria_actual} para {jugador2}")
                    continue

                pregunta_aleatoria = random.choice(preguntas_no_usadas)
                preguntas_usadas_2.append(pregunta_aleatoria)

                print(f"Categoría: {categoria_actual}")
                print(pregunta_aleatoria["pregunta"])
                for opcion in pregunta_aleatoria["opciones"]:
                    print(opcion)

                respuesta_usuario = input("¿Cuál es tu respuesta? (A/B/C/D): ").upper()

                if respuesta_usuario == pregunta_aleatoria["respuesta"]:
                    print("¡Correcto!")
                    puntaje_2 += 1
                    break
                else:
                    print("¡Incorrecto!")
                    break

            print(f"{jugador2} tiene {puntaje_2} puntos.\n")

        # Final del juego
        if puntaje_1 >= 6:
            print(f"{jugador1} ha ganado el juego!")
        elif puntaje_2 >= 6:
            print(f"{jugador2} ha ganado el juego!")
def guemes():
    
    puntaje = 0

    
    print("Bienvenido a esta aventura histórica, las reglas son muy sencillas: \n A lo largo del recorrido te encontrarás con distintas situaciones, dónde deberás elegir el camino que te parezca correcto. \n Deberás presionar el número 1 o 2 para elegir como continuar.")
    
    print("\n A tus jovenes 14 años te alistas como cadete a la Compañía del 3er. Batallón del Rey, del Regimiento Fixo. \n Pasaron 7 años de este acontecimiento y ocurrió un evento importante en el Virreinato del Río de la Plata, \n las famosas ""Invasiones Inglesas"", ante estas circunstancias te designaron un pelotón de Húsares. \n ¿Cómo desea proseguir?")
    print("\n 1. Tomar el mando y avanzar a toda velocidad hacia el navío británico que se encuentra encallado en el puerto de Buenos Aires \n 2. Guardar las distancias y esperar que los británicos bajen del barco.")

    eleccion = int(input("¿Cómo continuamos? "))

    if eleccion == 1:
        print("Sin darte cuenta, realizaste un acontecimiento único y se dice que fue el primero de la historia. \n ¡Nadie había tomado antes un navío con una carga de caballería!")
        print("Esta hazaña te ha dado un gran renombre y ganaste el respeto de tus hombres.") 
        puntaje += 10
    elif eleccion == 2:
        print("Decidiste no avanzar por miedo a que sea una masacre, mantuviste una línea defensiva y esperaste a que los ingleses se rindan. \n No fue una decisión desacertada pero tampoco destacaste entre tus tropas.")
        puntaje += 5
    else:
        print("Opción incorrecta.")

    print("------------------------------------------------------------------------------------- \n 4 años más tarde... \n Te encuentras con un pequeño número de gauchos en lo que denominan rumbo a la Quebrada de Humahuaca con el objetivo de atraer nuevas regiones al bando revolucionario de la Junta de Mayo.")
    print("\n Observas a lo lejos una partida de realistas, los superan en número y armamento, se dificulta poder huir sin que los descubran. Pero confías en tus soldados.")
    print("1. Avanzar directamente sobre el enemigo, aprovechando la velocidad de los caballos.")
    print("\n2. Esconderse en el monte y esperar que los realistas avancen para realizar una emboscada.")

    eleccion = int(input("¿Qué deseas hacer?"))

    if eleccion == 1:
        print("A pesar de contar con ventaja númerica y armamentística decidiste avanzar, confiando en la habilidad de tus hombres. \n Lograste salir victorioso, pero hubo varias bajas entre tus tropas.")
        puntaje += 1
    elif eleccion == 2:
        print("De manera inteligente, junto a tus tropas se escondieron en la maleza y el monte. \n Cuando las tropas realistas se encontraban a pocos metros, decidieron atacar sorpresivamente. Infundiendo pánico y muchas bajas en las tropas enemigas. \n De esta manera, pudieron proseguir hacia Huamhuaca de una manera totalmente segura.")
        print("Tras esta gran victoria, pudiste seguir con tus gauchos hacia Humahuaca")
        print("Antonio Chiclana (gobernador de Salta), en virtud de tus méritos, te designa Teniente de Granaderos de Fernando VII")
        puntaje +=10
    else:
        print("Opción incorrecta.")
       
    print("4 años después de lo acontecido, José de San Martín te reconoce como General en jefe del Ejército del Norte. \n Y se te ordena que en esta condición te dirijas a las avanzadas del Río Pasaje.")
    print("Desde esa posición debes avanzar hacia el Tuscal de Velarde al Coronel Saturnino Castro")
    print("Ahora bien, debes decidir si atacar de forma inmediata para no darle tiempo al enemigo de prepararse. \n O puedes optar por esperar que el enemigo ataque.")
    print("1. Atacar de forma inmediata. \n 2. Esperar que el enemigo ataque.")

    eleccion = int(input("¿Cómo avanzar?"))

    if eleccion == 1:
        print("Decidiste esperar al ataque enemigo, sin embargo, esto les dio tiempo a recibir refuerzos desde el Alto Perú. \n Ahora te encuentras en una situación vulnerable y en desventaja númerica. \n Sin embargo, lograste salir de la batalla ileso, muchos de tus hombres no contaron con esa suerte.")
        puntaje += 5
    elif eleccion == 2:
        print("Decidiste avanzar sobre las tropas enemigas antes de que puedan prepararse. \n Tiene que ser un ataque rápido y bien preparado debido a que no existe una ventaja númerica o armamentística importante.")
        "De manera inteligente decidiste que tus tropas blandieran lanzas, sables y boleadoras. \n Por más que te quisieron convencer que las armas de fuego infligían mucho más daño, los mosquetes no se llevan bien con los caballos."
        puntaje +=10
    else:
        print("Opción incorrecta.")
    
    
    print("Ahora debes tomar una decisión crucial mientras el enemigo se repliega hacia una nueva posición. \n Debes decidir si realizar una maniobra de pinza, dividiendo tus tropas y atacar por los flancos. \n O puedes avanzar directamente de frente con la fuerza de tu caballería, aprovechando el pavor del avance.")

    print("1. Aplicar maniobra de pinza. \n 2. Cargar en vanguardia.")
        
        
    eleccion = input("¿Aplicar una maniobra de pinza o cargar en vanguadia?")

    if eleccion == 1:
        print("Decidiste dividir tus tropas y avanzar por los flancos, una estrategia magistral. \n Los realistas nunca esperaron este ataque y fueron derrotados ")
        print("Sorprendentemente no perdiste a ninguno de tus soldados y lograron asegurar la zona.")        
        puntaje += 10
    elif eleccion == 2:
        print("Decidiste avanzar directamente con tus tropas montadas hacia la vanguardia. \n Los realistas pudieron disparar algunas ráfagas y se perdieron varias tropas, tal vez no fue la mejor estrategia. \n No obstante, saliste victorioso de este combate aunque la moral quedó tocada.")
        puntaje += 5
    else:
        print("Opción incorrecta.")

    print("Resultado final:")
    print("Puntaje total: ", puntaje)
   
    if puntaje > 15:
      print("¡Felicidades! Eres un verdadero gaucho aguerrido")
    else:
      print("Has ganado, pero podrías haberlo hecho mejor.")

    print("Fin de la historia")

print("BIENVENIDO AL MENU DE JUEGOS")
print("ELIGE ENTRE 'TU AVENTURA HISTORICA'(1) o 'PREGUNTADOS'(2)")

eleccion = int(input())

if eleccion == 1:
    print("Elige tu personaje: San Martín(1) o Guemes(2)")
    opcion_aventura = int(input())
    if opcion_aventura == 1:
        san_martin()
    elif opcion_aventura == 2:
        guemes()

elif eleccion == 2:
    preguntados()

