estado_actual = True

usuarios = {} #lista para almacenar a todos los usuarios del sistema,
              #están separados por tipo de usuario (estudiantes, profesores, admin)
              #Por lo tanto, cada conjunto de usuarios
              #es una lista y dentro habrá diccionarios
              #, cada diccionario es un usuario independiente.

              #Cada usuario tiene una clave "tipo_usuario"
              #que denomina su tipo (estudiante, profesor, admin)
              #con el propósito de: 
              # 1. organizar a los usuarios por tipo
              #,2.facilitar la gestión de sus datos.
              #,3. Al momento de desarrollar las funcionalidades de cada usuario,
              # podemos acceder a los datos de cada usuario según su tipo, 
              # lo que nos permite implementar funcionalidades específicas 
              # para cada tipo de usuario de manera más eficiente y estructurada.

              #Cómo se estructura el diccionario de usuarios si voy a
              #crear 3 listas aparte para cada tipo de usuario y que
              # guardarán los diccionarios de cada usuario?
              #usuarios = {
              #    "estudiantes": [ {usuario1}, {usuario2}, ... ],
              #    "profesores": [ {usuario1}, {usuario2}, ... ],
              #    "admin": [ {usuario1}, {usuario2}, ... ]
              #}
              #Cada usuario es un diccionario con sus datos, por ejemplo:
              #usuario1 = {
              #    "tipo_usuario": "estudiante",
              #    "nombre_usuario": "juan123",
              #    "contraseña": "password123",
              #    "otros_datos": "..."
              #}

              #Para aclarar: Creo la lista estudiantes = []
                                 #la lista admin = []
                                 #la lista profesores = []

        #Luego, agrego al diccionario usuarios
        #esas 3 listas vacias pero que tendrán diccionarios de usuarios, así:
        #usuarios['estudiantes'] = estudiantes
        #usuarios['admin'] = admin
        #usuarios['profesores'] = profesores
        #De esta manera, cada vez que el admin cree un nuevo usuario,
        #se agregará a la lista correspondiente según su tipo,
        #  y el diccionario usuarios mantendrá una estructura organizada para acceder 
        # a los datos de cada tipo de usuario de manera eficiente.

        # Se vería así:
        # usuarios = {
        #     "estudiantes": [ {usuario1}, {usuario2}, ... ],
        #     "profesores": [ {usuario1}, {usuario2}, ... ],
        #     "admin": [ {usuario1}, {usuario2}, ... ]
        # }

        #Y cada diccionario de usuario tendría una estructura como esta:
        # usuario1 = {
        #     "tipo_usuario": "estudiante",
        #     "nombre_usuario": "juan123",
        #     "contraseña": "password123",
        #     "otros_datos": "..."
        # }

        # Esta estructura facilita la gestión, ya que puedo:
        # acceder a los usuarios por tipo, 
        # implementar funcionalidades específicas para cada tipo de usuario,
        # y las funcionalidades las puedo crear condicionando las acciones
        # , es decir, que en cada acción use la clave "tipo_usuario" 
        # para determinar qué tipo de usuario puede hacer la acción 
        # y así ejecutar el código correspondiente a ese tipo de usuario.

        # Se crean en funciones las funcionalidades? o se crean en el mismo ciclo while?
        # Se crean en funciones para mantener el código organizado y modularizado,
        # lo que facilita su mantenimiento y escalabilidad.
        # Al crear funciones para cada funcionalidad, se puede:
        # 1. Reutilizar el código: Las funciones pueden ser llamadas 
        # desde diferentes partes del programa, 
        # lo que evita la duplicación de código.
        # 2. Mejorar la legibilidad: Las funciones permiten dividir el código en 
        # bloques lógicos.


        # El asunto está en saber cómo hacer la función y cómo condicionar el
        #código para que sólo se ejecute si el usuario tiene el tipo de usuario adecuado 
        # para esa funcionalidad.

        #Entonces hago un repaso breve y simple de lo que es una función y 
        # cómo se debe estructurar en este caso:
        # def nombre_funcion(parametros):
        #     # Código de la función
        #     return resultado

        # Para condicionar el código según el tipo de usuario, 
        # se puede usar una estructura condicional dentro de la función, por ejemplo:
        # def funcionalidad_especifica(usuarios):
        #     tipo_usuario = usuarios["tipo_usuario"]
        #     if tipo_usuario == "estudiante":
        #         # Código específico para estudiantes
        #     elif tipo_usuario == "profesor":
        #         # Código específico para profesores
        #     elif tipo_usuario == "admin":
        #         # Código específico para administradores
        #     else:
        #         print("Tipo de usuario no reconocido.")

        #Qué parametro recibe realmente la función? 
        # Recibe el diccionario de usuarios o 
        # recibe el usuario específico que está intentando ejecutar la funcionalidad?
        # La función debería recibir el usuario específico que está intentando 
        # ejecutar la funcionalidad,
        # ya que cada usuario tiene un tipo de usuario asociado,
        # lo que permite condicionar el código de la funcionalidad
        # según el tipo de usuario del usuario que está intentando ejecutarla.
        # Por ejemplo, si admin quiere crear un nuevo usuario, 
        # la función de creación de usuarios debería recibir el usuario 
        # admin, el cual fue validado en el login, y dentro de la función se
        #  puede verificar su tipo de usuario. Ejemplo:
        # def crear_usuario(admin_usuario):
        #     if admin_usuario["tipo_usuario"] == "admin":
        #         # Código para crear un nuevo usuario
        #     else:
        #         print("No tienes permisos para crear un nuevo usuario.")
        # El error de este ejemplo es que, la funcion no se puede ejecutar
        # porque antes ya se validó de acuerdo al login qué funcione se ejecutaran.
        # Entonces, la función no necesita recibir el usuario específico,
        # sino que la función se ejecuta sólo si el usuario tiene 
        # el tipo de usuario adecuado. Entonces el denominador común es:
        # el nombre de usuario que ingrese en el login, se compara con el nombre
        # de usuario en el diccionario de usuarios, y si coincide, se ejecuta la función
        # correspondiente a ese tipo de usuario. Por ejemplo:

        # def ejecutar_funcionalidad(usuarios, nombre_usuario):
        #     for tipo_usuario, lista_usuarios in usuarios.items():
        #         for usuario in lista_usuarios:
        #             if usuario["nombre_usuario"] == nombre_usuario:
        #                 if tipo_usuario == "estudiantes":
        #                     # Código específico para estudiantes
        #                 elif tipo_usuario == "profesores":
        #                     # Código específico para profesores
        #                 elif tipo_usuario == "admin":
        #                     # Código específico para administradores
        #                 return
        #     print("Usuario no encontrado.")
        # En este ejemplo, la función recibe el diccionario de usuarios y 
        # el nombre de usuario que se ingresó en el login. 
        # La función busca el usuario en el diccionario de usuarios,
        #  y si lo encuentra, ejecuta el código específico para su tipo de usuario. 
        # Si no encuentra el usuario, muestra un mensaje indicando que 
        # el usuario no fue encontrado.
        # Esta forma de hacerlo sirve para funcionalidades que pueden hacer
        # los tres tipos de usuario, pero si la funcionalidad es exclusiva 
        # para un tipo de usuario, entonces se puede condicionar la 
        # ejecución de la función directamente en el login, es decir, 
        # que sólo se ejecute la función si el usuario tiene el tipo de usuario adecuado. Por ejemplo:
        # if tipo_usuario == "estudiantes":
        #     ejecutar_funcionalidad_estudiantes()
        # elif tipo_usuario == "profesores":
        #     ejecutar_funcionalidad_profesores()
        # elif tipo_usuario == "admin":
        #     ejecutar_funcionalidad_admin()
        # De esta manera, se evita la necesidad de verificar 
        # el tipo de usuario dentro de la función, ya que la función 
        # sólo se ejecuta si el usuario tiene el tipo de usuario adecuado.



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
        
    continue_input = input("¿Deseas continuar? (si/no): ")
    if continue_input.lower() != "si":
        estado_actual = False
        print("¡Gracias por usar el Sistema Académico. ¡Adiós!")
