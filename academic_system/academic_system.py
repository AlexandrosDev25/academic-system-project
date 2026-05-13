estado_actual = True

usuarios = {}

estudiantes = []

admin = []

profesores = []

usuarios['estudiantes'] = estudiantes
usuarios['admin'] = admin
usuarios['profesores'] = profesores

while estado_actual:
    print("¡Bienvenido al Sistema Académico!")
    print("¿Qué tipo de usuario eres?")
    print("1. Estudiante")
    print("2. Profesor")
    print("3. Administrador")

    op = str(input("Por favor, ingresa el número correspondiente a tu rol: "))
    #elegir un rol de usuario
    
    match op:
        case "1":
            print("¡Bienvenido, Estudiante!")
            username = input("Ingresa tu nombre de usuario: ")
            password = input("Ingresa tu contraseña: ")
            usuarios["estudiantes"][username] = password
            print("Has iniciado sesión exitosamente como Estudiante.")

        case "2":
            print("¡Bienvenido, Profesor!")
            username = input("Ingresa tu nombre de usuario: ")
            password = input("Ingresa tu contraseña: ")
            usuarios["profesores"][username] = password
            print("Has iniciado sesión exitosamente como Profesor.")

        case "3":
            print("¡Bienvenido, Administrador!")
            username = input("Ingresa tu nombre de usuario: ")
            password = input("Ingresa tu contraseña: ")
            usuarios["admin"][username] = password
            print("Has iniciado sesión exitosamente como Administrador.")
        case _:
                print("Entrada inválida. Por favor, intenta de nuevo.")

    for key, value in usuarios.items():
        print(f"{key.capitalize()}: {value}")
        
    continue_input = input("¿Deseas continuar? (sí/no): ")
    if continue_input.lower() != "sí":
        estado_actual = False
        print("¡Gracias por usar el Sistema Académico. ¡Adiós!")
