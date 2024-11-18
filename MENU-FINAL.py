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
    print("\n 1. Tomar el mando y avanzar a toda velocidad hacia el navío británico que se encuentra encallado en el puerto de Buenos Aires. \n 2. Guardar las distancias y esperar que los británicos bajen del barco.")

    eleccion = int(input("¿Cómo continuamos? "))

    if eleccion == 1:
        print("Sin darte cuenta, realizaste un acontecimiento único y se dice que fue el primero de la historia. \n ¡Nadie había tomado antes un navío con una carga de caballería!")
        print("\nEsta hazaña te ha dado un gran renombre y ganaste el respeto de tus hombres.") 
        puntaje += 10
    elif eleccion == 2:
        print("Decidiste no avanzar por miedo a que sea una masacre, mantuviste una línea defensiva y esperaste a que los ingleses se rindan. \n No fue una decisión desacertada pero tampoco destacaste entre tus tropas.")
        puntaje += 5
    else:
        print("Opción incorrecta.")

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------ \n4 años más tarde... \nTe encuentras con un pequeño número de gauchos rumbo a la Quebrada de Humahuaca con el objetivo de atraer nuevas regiones al bando revolucionario de la Junta de Mayo.")
    print("\nObservas a lo lejos una partida de realistas, los superan en número y armamento, se dificulta poder huir sin que los descubran. Pero confías en tus soldados.")
    print("1. Avanzar directamente sobre el enemigo, aprovechando la velocidad de los caballos.")
    print("2. Esconderse en el monte y esperar que los realistas avancen para realizar una emboscada.")

    eleccion = int(input("¿Qué deseas hacer?"))

    if eleccion == 1:
        print("A pesar de contar con ventaja númerica y armamentística decidiste avanzar, confiando en la habilidad de tus hombres. \nLograste salir victorioso, pero hubo varias bajas entre tus tropas.")
        puntaje += 1
    elif eleccion == 2:
        print("De manera inteligente, junto a tus tropas se escondieron en la maleza y el monte. \nCuando las tropas realistas se encontraban a pocos metros, decidieron atacar sorpresivamente. Infundiendo pánico y muchas bajas en las tropas enemigas. \nDe esta manera, pudieron proseguir hacia Humahuaca de una manera totalmente segura.")
        print("Tras esta gran victoria, pudiste seguir con tus gauchos hacia Humahuaca")
        print("Antonio Chiclana (gobernador de Salta), en virtud de tus méritos, te designa Teniente de Granaderos de Fernando VII.")
        puntaje +=10
    else:
        print("Opción incorrecta.")
       
    print("4 años después de lo acontecido, José de San Martín te reconoce como General en jefe del Ejército del Norte. \n Y se te ordena que en esta condición te dirijas a las avanzadas del Río Pasaje.")
    print("\nDesde esa posición debes avanzar hacia el Tuscal de Velarde para atacar al Coronel Saturnino Castro.")
    print("\nAhora bien, debes decidir si atacar de forma inmediata para no darle tiempo al enemigo de prepararse. \nO puedes optar por esperar que el enemigo ataque.")
    print("1. Esperar que el enemigo ataque. \n2. Atacar de forma inmediata.")

    eleccion = int(input("¿Cómo avanzar?"))

    if eleccion == 1:
        print("Decidiste esperar al ataque enemigo, sin embargo, esto les dio tiempo a recibir refuerzos desde el Alto Perú. \n Ahora te encuentras en una situación vulnerable y en desventaja númerica. \n Sin embargo, lograste salir de la batalla ileso, muchos de tus hombres no contaron con esa suerte.")
        puntaje += 5
    elif eleccion == 2:
        print("Decidiste avanzar sobre las tropas enemigas antes de que puedan prepararse. \nTiene que ser un ataque rápido y bien preparado debido a que no existe una ventaja númerica o armamentística importante.")
        print("De manera inteligente decidiste que tus tropas blandieran lanzas, sables y boleadoras. \nPor más que te quisieron convencer que las armas de fuego infligían mucho más daño, los mosquetes no se llevan bien con los caballos.")
        puntaje +=10
    else:
        print("Opción incorrecta.")
    
    
    print("Ahora debes tomar una decisión crucial mientras el enemigo se repliega hacia una nueva posición.\nDebes decidir si realizar una maniobra de pinza, dividiendo tus tropas y atacar por los flancos. \nO puedes avanzar directamente de frente con la fuerza de tu caballería, aprovechando el pavor del avance.")

    print("1. Aplicar maniobra de pinza.\n2. Cargar en vanguardia.")
        
        
    eleccion = int(input("¿Aplicar una maniobra de pinza o cargar en vanguadia?"))

    if eleccion == 1:
        print("Decidiste dividir tus tropas y avanzar por los flancos, una estrategia magistral. \nLos realistas nunca esperaron este ataque y fueron derrotados ")
        print("\nSorprendentemente no perdiste a ninguno de tus soldados y lograron asegurar la zona.")        
        puntaje += 10
    elif eleccion == 2:
        print("Decidiste avanzar directamente con tus tropas montadas hacia la vanguardia. \nLos realistas pudieron disparar algunas ráfagas y se perdieron varias tropas, tal vez no fue la mejor estrategia. \nNo obstante, saliste victorioso de este combate aunque la moral quedó tocada.")
        puntaje += 5
    else:
        print("Opción incorrecta.")

    

    print("Ahora te encuentras en el mes de abril del año 1815, Roundeau te encomienda la misión de atacar la vanguardia del ejército realista en el Puesto del Marqués.")
    print("El pequeño poblado se encuentra en Jujuy, hace demasiado calor y no hay muchos suministros con los cuales aguantar. \nObservas a lo lejos decenas de nativos aymaras.")
    print("1. Intentar comunicarse con los aymaras para probar suerte con los recursos y dejar exploradores en la zona. \n2. Ignorar a los pobladores, advertirles sobre la marcha realista y seguir esperando.")

    eleccion = int(input("¿Cuál es su decisión?"))

    if eleccion == 1:
        print("Lograste una buena comunicación con los Aymara, te ofrecieron suministros y hospitalidad, la moral de tus tropas subió y estan en óptimas condiciones para enfrentarse al enemigo.")        
        print("Si bien no ofrecieron tropas para la batalla, mostraron simpatías por tu persona y por el bando revolucionario.")
        print("Puedes observar a lo lejos como las tropas realistas van apróximandose a Puente Marqués...")
        puntaje += 10
    elif eleccion == 2:
        print("Decidiste advertirles a los Aymara sobre la marcha realista, los pobladores te agradecieron y decidieron pegarse la vuelta. \n Te ofrecieron ir a su poblado para reponer energías pero te negaste por si los realistas decidían avanzar.")
        print("El clima no ayudaba en la espera y las tropas empezaban a molestarse, no se amotinaron por respeto a tu figura.")
        print("Puedes observar a lo lejos como las tropas realistas van apróximandose a Puente Marqués...")
        puntaje += 0
    else:
        print("Opción incorrecta.")


    print("Ante el avance de los realistas por este terreno cruel, visualizas lo cansadas y desmotivadas que están las tropas enemigas vestidas de blanco con sus uniformes europeos.")
    print("El armamento con el que cuentas carece de armas de fuego, debes decidir como usar el terreno a tu favor.")
    print("1. Utilizar las laderas de las montañas para aprovechar los flancos y la velocidad de las montañas.")
    print("2. Aprovechar el agotamiento de las tropas realistas y la falta de moral, para atacar de forma rápida en terreno llano.")


    eleccion = int(input("¿Cómo desea atacar?"))

    if eleccion == 1:
        print("Decidiste esperar que los enemigos atraviesen un espacio estrecho para poder atacar con tu caballería por las laderas de las montañas. \nEs una gran idea, sin embargo, se trata de un terreno totalmente irregular donde los pozos y las piedras abundan.")
        print("Logran aplastar completamente a los realistas, fue un triunfo total. Sin embargo, se tuvieron que sacrificar varios caballos por diferentes heridas provocadas por el terreno.")
        print("Tras esta espectacular victoria, el Cabildo de Salta, a petición del pueblo de la ciudad, te designa Gobernador de la Intendencia de Salta. \n Es decir, ahora eres gobernador de las regiones de Salta, Jujuy y Tarija")
        
        puntaje += 5
    elif eleccion == 2:
        print("Decidiste esperar que las tropas enemigas se acercaran completamente al terreno llano y mientras tanto te acercas lentamente sin ser vistos.")
        print("Cuando los enemigos se encuentran en terreno propicio, cansados y sin moral, deciden atacar de forma rápida y contundente. Logrando una victoria sin bajas.")
        print("Tras esta magistral victoria, el Cabildo de Salta, a petición del pueblo de la ciudad, te designa Gobernador de la Intendencia de Salta. \nEs decir, ahora eres gobernador de las regiones de Salta, Jujuy y Tarija")

        puntaje += 10
    else:
        print("Opción incorrecta.")

    
    print("6 de Agosto de 1816: cómo Gobernador Intendente de Salta, juras a la Independencia de las Provincias Unidas de Sud América en la ciudad de Jujuy. \nEn diciembre volverás a jurar a favor de la independencia en tu ciudad natal.")
    print("Casi un año después de la independencia, las fuerzas españolas del General La Serna que estuvieron avanzando por el Alto Perú, ingresan en la ciudad de Salta.")
    print("Como gobernador y general de tus tropas debes decidir como proceder.")
    print("Tienes la opción de salir por detrás de la ciudad y sorprender a las tropas realistas por la retaguardia o preparar de forma rápida la defensa en la ciudad con barricadas.")
    print("1. Atacar por la retaguardia. \n2.Defender la ciudad.")

    eleccion = int(input("¿Deseas atacar o defender la ciudad?"))

    if eleccion == 1:
        print("Decidiste salir, con la mayor parte de tus tropas, de la ciudad para sorprender a las tropas enemigas.")
        print("Las tropas realistas no se imaginaron que serían atacados en una emboscada nocturna. Tus hombres se enfrentaron con total ferocidad y los españoles se replegaron inmediatamente.")
        print("Lograste una victoria absoluta ante las tropas del General La Serna.")
        
        puntaje += 10
    elif eleccion == 2:
        print("Decidiste preparar barricadas improvisadas en las principales calles de la ciudad, pero las tropas realistas venían mejor equipadas en cuánto al armamento a distancia. \nLograron atravesar algunas calles pero la valentía de tus soldados y los vecinos de la ciudad trajeron como consecuencia la retirada enemiga.")
        print("Los vecinos de la ciudad se encargaron de enterrar tanto las tropas aliadas como enemigas y curar a los heridos.")
        print("Lograste una victoria parcial contra el General La Serna.")

        puntaje += 5
    else:
        print("Opción incorrecta.")

    print("Al ver como las tropas enemigas huyen, debes tomar una decisión rápida, si perseguir a los enemigos o mantenerse cauto para evitar sorpresas.")
    print("1. Perseguir a los realistas. \n2. Mantener la posición.")

    eleccion = int(input("¿Perseguir a los realistas o mantener la posición?"))

    if eleccion == 1:
        print("Decides avanzar sobre los enemigos que huyen para evitar que se reagrupen, muchos fueron tomados prisioneros y no lograron imponer resistencia.")
        print("El Director Supremo Pueyrredón dicta un decreto donde te premia con oro y una pensión vitalicia para tu hijo, reconociendo tus méritos en la batalla.")
        
        puntaje += 10
    elif eleccion == 2:
        print("Decides mantener la posición por miedo a que se trate de un ataque sorpresa. Sin embargo, no hay indicios de realistas durante los próximos días.")
        print("El Director Supremo Pueyrredón dicta un decreto donde te premia con oro y una pensión vitalicia para tu hijo, reconociendo tus méritos en la batalla.")

        puntaje += 5
    else:
        print("Opción incorrecta.")


    print("La batalla para mantener la independencia siguió durante varios años. En el año 1820 debiste tomar una decisión crucial para continuar con esta campaña.")
    print("La falta de recursos hacía cada vez más complicada la batalla, por lo que debías buscar nuevos fondos. \nAnte ello se mostraban dos posibilidades: \nObligar a los campesinos y gauchos a elevar sus impuestos para poder costear la guerra y en caso contrario arrebatar sus víveres o elevar los impuestos a los vecinos más pudientes.")
    print("1. Elevar los impuestos a los campesinos. \n2. Elevar los impuestos a los vecinos pudientes.")

    eleccion = int(input("¿Qué decisión deseas tomar?"))

    if eleccion == 1:
        print("El Cabildo de Salta (a  tú requerimiento) establece una nueva contribución forzosa, a cargo de campesinos, artesanos y trabajadores rurales.")
        print("\nEsto provoca la hostilidad de tus tropas y la mayoría de la población, fue una decisión terrible y varios de tus hombres desertaron.")
        
        
        puntaje -= 15 
    elif eleccion == 2:
        print("El Cabildo de Salta (a  tú requerimiento) establece una nueva contribución forzosa, a cargo de hacendados, comerciantes y demás vecinos pudientes.")
        print("\nSi bien esta decisión acentuó la antipatía de la oligarquía salteña, lograste un buen botín para proseguir con la campaña libertadora.")

        puntaje += 10
    else:
        print("Opción incorrecta.")

    print("Año 1821: te encuentras batallando en el norte de la provincia de Salta.") 
    print("\nLa mayoría de los miembros del Cabildo de Salta se pronuncian tu contra, declarando que dejaste el cargo de gobernador de la Intendencia.")
    print("\nAnte esta situación decides volver a la ciudad y logras que el pueblo salteño te apoye. Quiénes te quisieron echar del poder huyen hacia el campamento del jefe realista Olañeta.")
    print("\n En la semana siguiente, los realistas se escabullen en la ciudad con el apoyo de la oligarquía salteña y logran emboscarte durante la noche mientras duermes.")
    print("\nCon la ayuda de los pocos hombres que quedan en la ciudad huyes pero te hieren de gravedad, diez días después mueres a causa de la misma.")
    

    eleccion = int(input("Presiona 1 o 2 para quedar en la gloria de la historia Argentina."))

    if eleccion == 1:
        print("Tus restos son sepultados en la capilla de El Chamical.")
        print("\nFuiste el ejemplo de muchos y uno de los mayores próceres del país.")
        print("\n Tus soldados seguirán combatiendo hasta la futura expulsión de los realistas y la Independencia total de los países sudamericanos.")
        
        puntaje += 10 
    elif eleccion == 2:
        print("Tus restos son sepultados en la capilla de El Chamical.")
        print("\nFuiste el ejemplo de muchos y uno de los mayores próceres del país.")
        print("\n Tus soldados seguirán combatiendo hasta la futura expulsión de los realistas y la Independencia total de los países sudamericanos.")
        puntaje += 10
    else:
        print("Opción incorrecta.")




    print("A lo largo de la aventura, se le ha dado un puntaje a cada acción que tomaste, según esta puntuación se le ha concedido un título que lo representa.")
    
    print("\nPuntaje total: ", puntaje)
   
    if puntaje > 70:
      print("¡Felicidades! Eres una verdadera representación del gran Martín Miguel de Güemes, honraste su memoria con decisiones adecuadas.")
    else:
      print("La campaña terminó y tomaste tanto decisiones adecuadas como algunas mejorables, sin embargo, esto no quita reconocerte como un gaucho aguerrido.")

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

