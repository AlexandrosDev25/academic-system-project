current_state = True

users_info = {
    "students": {},
    "teachers": {},
    "admins": {}
    #user roles
}
while current_state:
    print("Welcome to the Academic System!")
    print("What type of user are you?")
    print("1. Student")
    print("2. Teacher")
    print("3. Admin")

    op = str(input("Please enter the number corresponding to your role: "))
    #choosing a user role
    
    match op:
        case "1":
            print("Welcome, Student!")
            username = input("Insert ur username: ")
            password = input("Insert ur password: ")
            users_info["students"][username] = password
            print("You have successfully logged in as a Student.")

        case "2":
            print("Welcome, Teacher!")
            username = input("Insert ur username: ")
            password = input("Insert ur password: ")
            users_info["teachers"][username] = password
            print("You have successfully logged in as a Teacher.")

        case "3":
            print("Welcome, Admin!")
            username = input("Insert ur username: ")
            password = input("Insert ur password: ")
            users_info["admins"][username] = password
            print("You have successfully logged in as an Admin.")
        case _:
                print("Invalid input. Please try again.")

    for key, value in users_info.items():
        print(f"{key.capitalize()}: {value}")
        
    continue_input = input("Do you want to continue? (yes/no): ")
    if continue_input.lower() != "yes":
        current_state = False
        print("Thank you for using the Academic System. Goodbye!")
